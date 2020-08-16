from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tsms$', views.tsms_sms, name="default"),
]
