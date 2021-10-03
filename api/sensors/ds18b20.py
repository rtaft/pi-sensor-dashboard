import os

from sensors.file_based import FileBasedSensor

class DS18B20(FileBasedSensor):
    def __init__(self, name=None, path=None):
        FileBasedSensor.__init__(self, name=name, units='C', path=path, regexp='t=(\d*)', factor=.001)
        self.sensor_type = 'sensors.ds18b20.DS18B20'

def lookup(existing_config):
    path = "/sys/bus/w1/devices"
    existing_paths = []
    for sensor in existing_config:
        if 'path' in sensor:
            existing_paths.append(sensor['path'])

    folders = [folder for folder in os.listdir(path) if '28-' in folder]
    filtered = []
    for folder in folders:
        if '{}/{}/w1_slave'.format(path, folder) not in existing_paths:
            filtered.append(folder)
    if filtered:
        for i in range(len(filtered)):
            print('{}) {}'.format(i+1, filtered[i]))
        selection = int(input("Select Sensor: "))
        selected = "{}/{}/w1_slave".format(path, filtered[selection-1])
        name = input("Sensor Name: ")
        sensor = DS18B20(name, selected)
        return sensor.get_config()
    print ("No Sensors Found")
    return None