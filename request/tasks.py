from celery import shared_task
import paramiko
from .models import Log

@shared_task(name="task_name")
def send_configuration(ip_address, configuration_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote machine and change username and pass base on your machine
        ssh.connect(ip_address, username='your_username', password='your_pass')

        # Open an SFTP session to upload the configuration file
        with ssh.open_sftp() as sftp:
            sftp.put(configuration_path, 'config.yaml')

    except paramiko.AuthenticationException:
        # Handle authentication failure
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        # Handle general SSH connection issues
        print(f"SSH connection failed: {str(e)}")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SSH connection
        ssh.close()


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
