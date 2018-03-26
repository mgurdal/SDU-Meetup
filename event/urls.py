from django.conf.urls import url
from .views import *

urlpatterns = [
    url('$^', Main.as_view(), name='index'),
    url('^dashboard', Dashboard.as_view(), name='dashboard'),
    url('^datatabledata', DashboardDataTable.as_view(), name='datatable-data'),
    url('^signin', SigninWebSite.as_view(), name='signin')
]
