import paramiko

def run_docker_client(client_ip, username, password, docker_image):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(client_ip, username=username, password=password)

        command = f'docker run -v config.yaml:/workspace/config.yaml {docker_image}'
        stdin, stdout, stderr = ssh.exec_command(command)

        # Print stdout
        for line in stdout:
            print(f'STDOUT: {line.strip()}')

        # Print stderr
        for line in stderr:
            print(f'STDERR: {line.strip()}')

    except paramiko.AuthenticationException:
        print("Failed to authenticate with the client.")
    except paramiko.SSHException as e:
        print(f"SSH connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        ssh.close()
