import django_tables2 as tables
from django_tables2 import TemplateColumn, CheckBoxColumn
from .models import Partner, PartnerType

action_column = '''
<a 
    class="btn btn-success btn-sm"
    hx-get="{% url "partner:partner_update" record.id %}" 
    hx-trigger="click"
    hx-push-url="true" 
    hx-select="#main-div"
    hx-target="#content"
    hx-swap="innerHTML"
    hx-disabled-elt="find button"
    hx-indicator="#spinner"
    hx-target-5*="#error500"
    hx-target-404="#error400"
>
    <span class="bi bi-pencil-square"" aria-hidden="true"></span>
</a>

'''


class PartnerTable(tables.Table):
    selection = CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    edit = TemplateColumn(template_code=action_column)

    class Meta:
        model = Partner
        template_name = "partners/bootstrap_htmx.html"
        fields = ('id', 'name', 'trade_name', 'partner_type', 'person_type', 'federal_id')
        sequence = ('selection', 'id', 'name', 'trade_name', 'partner_type', 'person_type', 'federal_id', 'edit')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns['selection'].column.attrs = {"td":{"style" : "width:5%;" }}
        self.columns['name'].column.attrs = {"td":{"style" : "width:10%;" }}
        self.columns['name'].column.attrs = {"td":{"style" : "width:15%;" }}
        self.columns['trade_name'].column.attrs = {"td":{"style" : "width:5%;" }}
        self.columns['partner_type'].column.attrs = {"td":{"style" : "width:10%;" }}
        self.columns['person_type'].column.attrs = {"td":{"style" : "width:10%;" }}
        self.columns['federal_id'].column.attrs = {"td":{"style" : "width:10%;" }}
        self.columns['edit'].column.attrs = {"td":{"style" : "width:5%;" }}



action_column_type = '''
<a 
    class="btn btn-success btn-sm"
    hx-get="{% url "partner:partner_type_update" record.id %}" 
    hx-trigger="click"
    hx-push-url="true" 
    hx-select="#main-div"
    hx-target="#content"
    hx-swap="innerHTML"
    hx-disabled-elt="find button"
    hx-indicator="#spinner"
    hx-target-5*="#error500"
    hx-target-404="#error400"
>
    <span class="bi bi-pencil-square"" aria-hidden="true"></span>
</a>

'''


class PartnerTypeTable(tables.Table):
    selection = CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    edit = TemplateColumn(template_code=action_column_type)

    class Meta:
        model = PartnerType
        template_name = "partners/bootstrap_htmx.html"
        fields = ('id', 'name',)
        sequence = ('selection', 'id', 'name', 'edit')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.columns['selection'].column.attrs = {"td":{"style" : "width:5%;" }}
        self.columns['name'].column.attrs = {"td":{"style" : "width:10%;" }}
        #self.columns['edit'].column.attrs = {"td":{"style" : "width:5%;" }}