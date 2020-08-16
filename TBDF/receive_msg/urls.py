from django.conf.urls import url
from django.urls import path
from receive_msg import views

urlpatterns = [
    path('btn', views.button, name='btn'),
    path('frm', views.output, name='frm'),
]