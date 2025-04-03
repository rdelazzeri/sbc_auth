from django.urls import path
from . import views as v

app_name = 'partner'

urlpatterns = [
    #Partner
    path('partner/new', v.PartnerCreate.as_view(), name='partner_new'),
    path('partner/newac', v.PartnerCreateAC.as_view(), name='partner_new_ac'),
    path('partner/<str:pk>', v.PartnerUpdate.as_view(), name='partner_update'),
    path('partner/<str:pk>/delete', v.PartnerDelete.as_view(), name='partner_delete'),
    path('partners', v.PartnerList.as_view(), name='partner_list'),
    path('partners/table', v.PartnerHTMxTableView.as_view(), name='partner_htmx'),
    path('partners/bulk', v.PartnersBulkAction.as_view(), name='partners_bulk_action'),

    path('type/new', v.PartnerTypeCreate.as_view(), name='partner_type_new'),
    path('type/modal-new', v.PartnerTypeModalCreate.as_view(), name='partner_type_modal_new'),
    path('type/<str:pk>/modal-update', v.PartnerTypeModalUpdate.as_view(), name='partner_type_modal_update'),
    path('type/<str:pk>', v.PartnerTypeUpdate.as_view(), name='partner_type_update'),
    path('types', v.PartnerTypeList.as_view(), name='partner_type_list'),
]