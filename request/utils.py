import yaml

def parse_configuration(file_path):
    with open(file_path, 'r') as file:
        configuration = yaml.safe_load(file)
    return configuration

