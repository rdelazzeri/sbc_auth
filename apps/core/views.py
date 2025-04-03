from typing import Any
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.utils.translation import gettext as _


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        #data['custom_css'] = '/static/blue-voltage.css'
        return data
    

class UserData(TemplateView):
    template_name = 'core/user_data.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['username'] = self.request.user.username
        data['email'] = self.request.user.email
        data['tenant'] = self.request.tenant_id
        data['tenant_name'] = self.request.tenant.name if self.request.tenant else None
        data['user'] = self.request.user
        data['user_id'] = self.request.user.id  
        return data


class TestMenu(TemplateView):
    template_name = 'core/menu.html'

class SideMenu(TemplateView):
    template_name = 'core/menu.html'
    menu = [
            {
                'hasChildren': False,
                'link': '/',
                'text': _('Home'),
                'image': 'fs-4 bi-house',
            },
            {
                'hasChildren': True,
                'text': _('Partners'),
                'image': 'fa fa-users',
                'children':[
                    {
                        'link': '/part/partners',
                        'text': _('Partners'),
                    },
                    {
                        'link': '/part/partner/new',
                        'text': _('New Partner'),
                    },
                    {
                        'link': '/part/types',
                        'text': _('Partner types'),
                    },
                    {
                        'link': '/part/type/new',
                        'text': _('New partner type'),
                    },

                ]
            },
            {
                'hasChildren': True,
                'text': 'Products',
                'image': 'fa fa-cogs',
                'children':[
                    {
                        'link': '/prod/products',
                        'text': _('Products'),
                    },
                    {
                        'link': '/prod/product/new',
                        'text': _('New Product'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('Groups'),
                    },
                    {
                        'link': '/prod/group/new',
                        'text': _('New group'),
                    },

                ]
            },
            {
                'hasChildren': True,
                'text': _('Commercial'),
                'image': 'fa fa-handshake',
                'children':[
                    {
                        'link': '/com/orders',
                        'text': _('Orders'),
                    },
                    {
                        'link': '/com/orders/new',
                        'text': _('New Order'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('MRP'),
                    },

                ]
            },
            {
                'hasChildren': True,
                'text': _('Purshaise'),
                'image': 'fa fa-shopping-cart',
                'children':[
                    {
                        'link': '/prod/products',
                        'text': _('Production Order'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('Material'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('MRP'),
                    },

                ]
            },
            {
                'hasChildren': True,
                'text': _('Production'),
                'image': 'fa fa-industry',
                'children':[
                    {
                        'link': '/prod/products',
                        'text': _('Production Order'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('Material'),
                    },
                    {
                        'link': '/prod/groups',
                        'text': _('MRP'),
                    },

                ]
            },
            {
                'hasChildren': True,
                'text': _('Finances'),
                'image': 'fa fa-usd',
                'children':[
                    {
                        'link': '/part/partners',
                        'text': 'Partners',
                    },
                    {
                        'link': '/prod/groups',
                        'text': 'Groups',
                    },
                    {
                        'link': '/prod/products',
                        'text': 'Produtos',
                    },

                ]
            },


            {
                'hasChildren': True,
                'text': _('Todos'),
                'image': 'fa fa-check-square',
                'children':[
                    {
                        'link': '/part/partners',
                        'text': 'Partners',
                    },
                    {
                        'link': '/prod/groups',
                        'text': 'Groups',
                    },
                    {
                        'link': '/prod/products',
                        'text': 'Produtos',
                    },

                ]
            },
            {
                'hasChildren': False,
                'link': '/com/orders',
                'text': _('Finances'),
                'image': 'fa fa-usd',
            },

        ]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)    
        data['menu'] = self.menu
        return data
    








class CustonCreateView(CreateView):

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
