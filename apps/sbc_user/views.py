# View de Login Personalizada
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.views.generic.edit import CreateView
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from .forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView as AuthPasswordChangeView
from .forms import CustomPasswordChangeForm



class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'sbc_user/create_user.html'
    success_url = reverse_lazy('sbc_user:create_user_success')


class UserCreateSuccessView(TemplateView):
    template_name = 'sbc_user/create_user_success.html'


class PasswordChangeView(AuthPasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'sbc_user/change_password.html'
    success_url = reverse_lazy('sbc_user:change_password_success')


class PasswordChangeSuccessView(TemplateView):
    template_name = 'sbc_user/change_password_success.html'


class PasswordResetView(View):
    form_class = PasswordResetForm
    template_name = 'sbc_user/reset_password.html'
    success_url = reverse_lazy('sbc_user:reset_password_success')

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
    template_name = 'sbc_user/reset_password_success.html'


class DashboardView(TemplateView):
    template_name = 'sbc_user/dashboard.html'

