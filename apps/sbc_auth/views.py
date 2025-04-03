# View de Login Personalizada
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.tenant.models import Tenant
from .models import User
from apps.tenant.models import UserTenant
from django.views.generic.edit import CreateView
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from .forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView as AuthPasswordChangeView
from .forms import CustomPasswordChangeForm


def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        tenant_name = request.POST.get('tenant')
        tenant = None
        
        if tenant_name:
            try:
                tenant = Tenant.objects.get(name=tenant_name)
            except Tenant.DoesNotExist:
                tenant = None

        user = authenticate(request, email=email, password=password)
    
        if user is not None:
            if tenant:
                # Verifica se o usuário está associado ao tenant
                if UserTenant.objects.filter(user=user, tenant=tenant, is_active=True).exists():
                    login(request, user)
                    request.session['tenant_id'] = tenant.id
                    return redirect('core:dashboard')
            else:
                login(request, user)
        else:
            return HttpResponse("Credenciais inválidas")
    
    return render(request, 'sbc_auth/login.html')



class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'sbc_auth/create_user.html'
    success_url = reverse_lazy('sbc_auth:create_user_success')


class UserCreateSuccessView(TemplateView):
    template_name = 'sbc_auth/create_user_success.html'




class PasswordChangeView(AuthPasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'sbc_auth/change_password.html'
    success_url = reverse_lazy('sbc_auth:change_password_success')

class PasswordChangeSuccessView(TemplateView):
    template_name = 'sbc_auth/change_password_success.html'




class PasswordResetView(View):
    form_class = PasswordResetForm
    template_name = 'sbc_auth/reset_password.html'
    success_url = reverse_lazy('sbc_auth:reset_password_success')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                user.set_password('1234')  # Set the default password
                user.save()
                return redirect(self.success_url)
            except User.DoesNotExist:
                form.add_error('email', 'User with this email does not exist.')
        return render(request, self.template_name, {'form': form})

class PasswordResetSuccessView(TemplateView):
    template_name = 'sbc_auth/reset_password_success.html'


class DashboardView(TemplateView):
    template_name = 'sbc_auth/dashboard.html'

class TenantSwitchView(View):
    template_name = 'sbc_auth/switch_tenant.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_tenants = UserTenant.objects.filter(user=user, is_active=True)
        current_tenant_id = request.session.get('tenant_id')
        current_tenant = Tenant.objects.get(id=current_tenant_id) if current_tenant_id else None
        return render(request, self.template_name, {
            'user_tenants': user_tenants,
            'current_tenant': current_tenant
        })

    def post(self, request, *args, **kwargs):
        tenant_id = request.POST.get('tenant_id')
        if tenant_id:
            request.session['tenant_id'] = tenant_id
            return redirect('sbc_auth:dashboard')
        user = request.user
        user_tenants = UserTenant.objects.filter(user=user, is_active=True)
        current_tenant_id = request.session.get('tenant_id')
        current_tenant = Tenant.objects.get(id=current_tenant_id) if current_tenant_id else None
        return render(request, self.template_name, {
            'user_tenants': user_tenants,
            'current_tenant': current_tenant,
            'error': 'Please select a tenant.'
        })