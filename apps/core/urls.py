from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    #Partner
    path('', v.Index.as_view(), name='index'),
    path('welcome', v.Index.as_view(), name='index'),
    path('side_menu', v.SideMenu.as_view(), name='side_menu'),
    path('user-data', v.UserData.as_view(), name='user_data'),
    path('test', v.TestMenu.as_view(), name='test_menu'),

]
