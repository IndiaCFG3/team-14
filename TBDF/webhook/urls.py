from django.urls import path,include
from webhook import views

urlpatterns = [
    path('webhook',views.webhook, name='webhook'),
]
