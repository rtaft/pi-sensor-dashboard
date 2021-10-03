import json

SENSOR_CONFIG_FILE="sensors.json"
DATABASE_CONFIG_FILE="database.json"
API_PORT=9000

def get_config(filename=None):
    try:
        if not filename:
            filename = SENSOR_CONFIG_FILE
        with open(filename) as config_file:
            data = json.load(config_file)
        return data
    except FileNotFoundError:
        return []

def save_config(filename, config):
    with open(filename, 'w') as config_file:
        json.dump(config, config_file, indent=4)
        config_file.flush()
        config_file.close()

 