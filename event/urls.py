from django.conf.urls import url
from .views import Main,Dashboard

urlpatterns = [
    url('$^', Main.as_view(), name='index'),
    url('^dashboard', Dashboard.as_view(), name='dashboard')
]
