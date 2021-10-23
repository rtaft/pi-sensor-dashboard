from sensor_service import SensorService
from sensors.mcp3008 import AnalogSensor, MCP3008
from sensors.file_based import FileBasedSensor
from sensors.ds18b20 import DS18B20
import importlib
import pkgutil
from threading import Thread

import app_config
from api.restful import API, APP #, SOCK
from routing import route


def main():
    sensor_service = SensorService()
    kwargs = dict(host='0.0.0.0', port=app_config.API_PORT, debug=False, threaded=True)
    route(sensor_service)
    flaskThread = Thread(target=APP.run, daemon=True, kwargs=kwargs).start()
    sensor_service.run_collection_service()



if __name__ == "__main__": 
    main()