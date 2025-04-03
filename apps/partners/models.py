from django.db import models
from django.db.models.deletion import PROTECT, CASCADE
from django.conf import settings
from django.utils.translation import gettext as _
from autocomplete import  ModelAutocomplete, register
from apps.core.models import BaseModel


PERSON_TYPE_CHOICES = (('N', _('Natural')), ('L', _('Legal')))

class Country(BaseModel):
    name = models.CharField(_("Country name"), max_length=60, unique=True)
    cod = models.CharField(_("Country cod"), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class DocumentType(BaseModel):
    name = models.CharField(_("Document Type Name"), max_length=60, unique=True)
    description = models.CharField(_("Document Type Description"), max_length=100, blank=True, null=True)
    type = models.CharField(_("Document Type"), max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name

class PartnerDocument(BaseModel):
    partner = models.ForeignKey('Partner', verbose_name=_("Partner"), on_delete=CASCADE, blank=True, null=True)
    document_type = models.ForeignKey('DocumentType', verbose_name=_("Document Type"), on_delete=CASCADE, blank=True, null=True)
    number = models.CharField(_("Document Number"), max_length=30)

    def __str__(self):
        return self.name


class PhoneMask(BaseModel):
    partner = models.ForeignKey('Partner', verbose_name=_("Partner"), on_delete=CASCADE, blank=True, null=True)
    name = models.CharField(_("Document Number"), max_length=30)


class PhoneNumber(BaseModel):
    partner = models.ForeignKey('Partner', verbose_name=_("Partner"), on_delete=CASCADE, blank=True, null=True)
    name = models.CharField(_("Document Number"), max_length=30)
    number = models.CharField(_("Document Number"), max_length=30)

    def __str__(self):
        return self.name
    


class Partner(BaseModel):
    name = models.CharField(_("Name"), max_length=120)
    partner_type = models.ManyToManyField('PartnerType', verbose_name=_("Partner Type"), blank=True)
    person_type = models.CharField(_('Person Type'), max_length=2, choices=PERSON_TYPE_CHOICES, default='L',)
    trade_name = models.CharField(_('Trade Name'),max_length=100, blank=True, null=True)
    federal_id = models.CharField(_('Federal Tax Id'),max_length=20,  blank=True, null=True)
    state_id = models.CharField(_('State Tax Id'),max_length=20,  blank=True, null=True)
    ssn = models.CharField(_('Social Security Number'), max_length=20,  blank=True, null=True)
    phone1 = models.CharField(max_length=15, blank=True, null=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    obs = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.name
    

class PartnerType(BaseModel):
    name = models.CharField(_("Partner Type Name"), max_length=60)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print('custon save partene')
        user = kwargs.pop('user', None)
        print(user)
        # Set the author to the current user before saving
        if not self.pk:  # Check if it's a new instance
            print('no pk')
            user = kwargs.pop('user', None)
            print(user)
        else:
            print('pk')
        super().save(*args, **kwargs)
    

@register
class PartnerAutocomplete(ModelAutocomplete):
    model = Partner
    search_attrs = [ 'name' ]

@register
class PartnerTypeAutocomplete(ModelAutocomplete):
    model = PartnerType
    search_attrs = [ 'name' ]
    minimum_search_length = 0
    