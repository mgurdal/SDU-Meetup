from django.conf.urls import url
from .views import Main

urlpatterns = [
    url('$^', Main.as_view(), name='index'),
]
