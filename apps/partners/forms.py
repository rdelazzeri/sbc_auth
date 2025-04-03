from django import forms
from .models import *
from django.forms import inlineformset_factory
from autocomplete import Autocomplete, AutocompleteWidget, ModelAutocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Column, Row, Field, Div, Button, Fieldset, ButtonHolder, HTML
from crispy_forms.bootstrap import FormActions, PrependedText, AppendedText, StrictButton, FieldWithButtons
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        widgets = {
            "partner_type":  AutocompleteWidget(ac_class=PartnerTypeAutocomplete, options={"multiselect": True}),
        }
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'new-partner-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('partner:partner_new'),
            'hx-push-url': "true", 
            'hx-select': "#main-div",
            'hx-target': "#content",
            'hx-swap': "innerHTML",
            'hx-disabled-elt': "find button",
            'hx-indicator': "#spinner",
            'hx-disinherit': "*", # this is important to don't break htmx-autocomplete
        }
        self.helper.layout = Layout(    
            Div(
                Row(
                    Field('name', wrapper_class='col-6'),
                    Field('trade_name', wrapper_class='col-6'),
                ),
                Row(
                    Field('partner_type', wrapper_class='col-6'),
                    Field('person_type', wrapper_class='col-6'),                    
                ),
                Row(
                    Field('federal_id', wrapper_class='col-4'),
                    Field('state_id', wrapper_class='col-4'),   
                    Field('ssn', wrapper_class='col-4'),                     
                ),
                Row(
                    Field('phone1', wrapper_class='col-6'),
                    Field('phone2', wrapper_class='col-6'),                    
                ),
                Row(
                    Field('email', wrapper_class='col-12'),                
                ),
                Row(
                    Field('obs', wrapper_class='col-12'),                 
                    css_id='modal'
                ),                
                css_class='m-2',
            ),
        )


class PartnerTypeForm(forms.ModelForm):
    class Meta:
        model = PartnerType
        fields = '__all__'
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'new-partner-type-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('partner:partner_type_new'),
            'hx-push-url': "false", 
            'hx-target': "#content",
            'hx-select': "#main-div",
            'hx-disinherit': "*", # this is important to don't break htmx-autocomplete
        }
        self.helper.layout = Layout(    
                Row(
                    Field('name', wrapper_class='col-12'),
                ),                
        )


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        count_name = PartnerType.objects.filter(name = name).count()

        if count_name > 0:
            raise ValidationError(
                    "This type is alredy registered."
                )




class PartnerTypeModalForm(forms.ModelForm):
    class Meta:
        model = PartnerType
        fields = '__all__'
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'new-partner-type-modal-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('partner:partner_type_modal_new'),
            'hx-push-url': "false", 
            'hx-target': "#base-modal",
            'hx-disabled-elt': "find button",
            'hx-indicator': "#spinner",
            'hx-disinherit': "*", # this is important to don't break htmx-autocomplete
        }
        self.helper.layout = Layout(    
                Row(
                    Field('name', wrapper_class='col-12'),
                ),                
        )


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        count_name = PartnerType.objects.filter(name = name).count()

        if count_name > 0:
            raise ValidationError(
                    "This type is alredy registered."
                )
        

class PartnersBulkActionForm(forms.Form):
    ids = forms.CharField(max_length=8)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'partners-bulk-action-modal-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('partner:partners_bulk_action'),
            'hx-push-url': "false", 
            'hx-target': "#base-modal",
            'hx-disabled-elt': "find button",
            'hx-indicator': "#spinner",
            'hx-disinherit': "*", # this is important to don't break htmx-autocomplete
        }
