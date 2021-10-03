import json

import app_config

def get_config():
    try:
        with open(app_config.SENSOR_CONFIG_FILE) as config_file:
            data = json.load(config_file)
        return data
    except FileNotFoundError:
        return []

def save_config(config):
    with open(app_config.SENSOR_CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)
        config_file.flush()
        config_file.close()

