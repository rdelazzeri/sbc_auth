from decimal import Decimal
from django.db.models import Q
import django_filters
from .models import Partner, PartnerType

class PartnerFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Partner
        fields = ['partner_type']

    def universal_search(self, queryset, name, value):
        return Partner.objects.filter(
            Q(name__icontains=value) | Q(trade_name__icontains=value)
        )
    
class PartnerTypeFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = PartnerType
        fields = '__all__'

    def universal_search(self, queryset, name, value):
        return Partner.objects.filter(
            Q(name__icontains=value) | Q(id__icontains=value)
        )