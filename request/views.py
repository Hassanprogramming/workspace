from django.shortcuts import render
from .tasks import send_configuration
from .utils import parse_configuration

# Create your views here.

def send_configuration_view(request):
    configuration = parse_configuration('config.yaml')
    ip_address = '192.168.1.2'  # client IP address
    send_configuration.delay(ip_address, configuration)
    return render(request, 'request/success.html')
