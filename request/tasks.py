from celery import shared_task
import paramiko
from .models import Log

@shared_task
def send_configuration(ip_address, configuration):
    # Use ssh_library to send the configuration to the client with the given IP address
    paramiko.send(ip_address, configuration)

@shared_task
def process_received_data(data):
    # Parse the received JSON data and save it to the database
    log = Log.objects.create(
        stream_id=data['stream_id'],
        timestamp=data['timestamp'],
        status=data['status'],
        type=data['log']['type'],
        coordinates=data['log']['coordinates'],
        thumbnail=data['log']['thumbnail'],
        session_id=data['session_id']
    )
    log.save()
