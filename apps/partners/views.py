from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView, DeleteView, UpdateView, CreateView, ListView, View, FormView
from django.urls import reverse_lazy, reverse
from django.template import loader
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import PartnerTable, PartnerTypeTable
from .filters import PartnerFilter, PartnerTypeFilter

'''
******************************************************************************
                                    Partner
******************************************************************************
'''


class PartnerList(SingleTableMixin, FilterView):
    table_class = PartnerTable
    queryset = Partner.objects.all()
    filterset_class = PartnerFilter
    paginate_by = 5
    template_name = "partners/partner_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = context['filter']
        form = filter.form             # <- here!
        form.helper = FormHelper()
        form.helper.disable_csrf = True
        return context


class PartnerHTMxTableView(SingleTableMixin, FilterView):
    table_class = PartnerTable
    queryset = Partner.objects.all()
    filterset_class = PartnerFilter
    paginate_by = 5

    def get_template_names(self):
        if self.request.htmx:
            template_name = "partners/partner_table_htmx_partial.html"
        else:
            template_name = "partners/partner_table_htmx.html"

        return template_name


class PartnersBulkAction(SuccessMessageMixin, FormView):
    form_class = PartnersBulkActionForm
    template_name = "partners/partner_bulk_modal.html"
    success_message = "Bulk actions was executed successfully"
    success_url = reverse_lazy('partner:partners_bulk_action')


    def get_initial(self):
        initial = super().get_initial()
        initial['ids'] = self.request.GET.getlist('id')
        return initial


class PartnerCreate(CreateView):
    model = Partner
    form_class = PartnerForm
    success_url = '/part/partners'


class PartnerCreateAC(CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partners/partner_form_ac.html'
    success_url = '/part/partners'


class PartnerUpdate(UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partners/partner_form.html'
    

class PartnerDelete(DeleteView):
    model = Partner
    success_url ="/part/partners"
    template_name = "part/partner_delete.html"






####Partner type
from ..core.views import CustonCreateView

class PartnerTypeCreate(SuccessMessageMixin,CreateView):
    model = PartnerType
    form_class = PartnerTypeForm
    template_name = 'partners/partnertype_form.html'
    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy('partner:partner_type_new')


class PartnerTypeUpdate(UpdateView):
    model = PartnerType
    form_class = PartnerTypeForm
    template_name = 'partners/partnertype_form.html'
    success_url = '/part/types'
    

class PartnerTypeModalCreate(SuccessMessageMixin, CreateView):
    model = PartnerType
    form_class = PartnerTypeModalForm
    template_name = 'partners/partnertype_modal_form.html'
    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy('partner:partner_type_modal_new')

    
class PartnerTypeModalUpdate(UpdateView):
    model = PartnerType
    form_class = PartnerTypeModalForm
    template_name = 'partners/partnertype_modal_form.html'


class PartnerTypeList(SingleTableMixin, FilterView):
    table_class = PartnerTypeTable
    queryset = PartnerType.objects.all()
    filterset_class = PartnerTypeFilter
    paginate_by = 5
    template_name = "partners/partnertype_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = context['filter']
        form = filter.form 
        form.helper = FormHelper()
        form.helper.disable_csrf = True
        return context


