from django.conf.urls import url
from django.urls import path

from tsms import views

urlpatterns = [
    path('tsms', views.tsms_sms, name='SMS'),
]
