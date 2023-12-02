# workspace
## About
Suppose a number of clients (given Docker) received data from the tools connected to them and after
The process is sent to the server (this process is mocked). The server is tasked with automatically connecting to the client
via ssh and running docker client with your config. Docker client, according to your config, send task
It is responsible for the data to the server. Data asynchronously to a desired celery task in your config
specified, are sent to the server. Please mount the configuration as follows:
docker run ... -v config.yaml:/workspace/config.yaml ...
Your task is to write a program using Redis, Celery, Django, Python that:
● Using Python and ssh, automatically send the necessary configuration to the client (with a predefined IP address)
Send it as desired and run it on the client machine based on the received configuration. After
Running, the existing docker will send the data to the server asynchronously.
● Receive the data sent from the clients on the server and save it on a database.
*** The format of each data sent is as follows (json):
{
"stream_id": 0, # Integer
"timestamp": "2023-11-13 15:00:16.868336", # Date of event
"status": "D", # 'D' for danger and 'S' for safe
"log": {
"type": "Person", # Object type: Person, Face, Bag
"coordinates": [1033, 262, 1904, 1077], # List of 4 integers
"thumbnail": "[image/base64]" # Base64 encoded image of object
},
"session_id": "db81021b-8edc-45c4-830b-a1229ffb4af3" # Session uuid
}
*** The configuration file received by Docker is as follows (yaml):
sender_config:
server_ip: "192.168.1.1" # IP of the Broker server
server_port: 6280 # Port of Broker Server
send_rate: 10 # An Integer that determines the time interval between
data transfer (milliseconds)
celery_task_name: "task_name" # Name of the task


## Getting Started

### Prerequisites

Before setting up Workspace, make sure you have the following installed:

- Python
- Docker
- Redis
- Other dependencies (list any additional requirements in requirements.txt)

### Installation

Clone the repository and install the required dependencies:

git clone https://github.com/Hassanprogramming/workspace.git
cd workspace
pip install -r requirements.txt
# after creaing your environment do those jobs.
