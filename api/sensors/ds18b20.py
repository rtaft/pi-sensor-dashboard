import os
from marshmallow import fields
from sensors.file_based import FileBasedSensor
from sensors.sensor import SensorSchema


DS18B20_PATH="/sys/bus/w1/devices/"

class DS18B20Schema(SensorSchema):
    path = fields.String(required=False, allow_none=False, metadata=dict(fieldname="Path", notes="Path to sensor readings file."))
    device = fields.String(required=False, allow_none=False, metadata=dict(fieldname="Path", notes="Path to sensor readings file."))

class DS18B20(FileBasedSensor):
    def __init__(self, name=None, path=None, device=None):
        if path:
            FileBasedSensor.__init__(self, name=name, units='C', path=path, regexp='t=(\d*)', factor=.001)
        elif device:
            FileBasedSensor.__init__(self, name=name, units='C', path=DS18B20_PATH + device, regexp='t=(\d*)', factor=.001)
            
        self.sensor_type = 'sensors.ds18b20.DS18B20'

def lookup(existing_config):
    existing_paths = []
    for sensor in existing_config:
        if 'path' in sensor:
            existing_paths.append(sensor['path'])

    folders = [folder for folder in os.listdir(DS18B20_PATH) if '28-' in folder]
    filtered = []
    for folder in folders:
        if '{}{}/w1_slave'.format(DS18B20_PATH, folder) not in existing_paths:
            filtered.append(folder)
    return filtered
    # TODO move to command.py
    # if filtered:
    #     for i in range(len(filtered)):
    #         print('{}) {}'.format(i+1, filtered[i]))
    #     selection = int(input("Select Sensor: "))
    #     selected = "{}/{}/w1_slave".format(path, filtered[selection-1])
    #     name = input("Sensor Name: ")
    #     sensor = DS18B20(name, selected)
    #     return sensor.get_config()
    # print ("No Sensors Found")
    # return None