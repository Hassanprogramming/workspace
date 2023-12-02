from django.urls import path, include
from .views import send_configuration_view

urlpatterns = [
    path('send-configuration/', send_configuration_view, name='send-configuration'),
]
