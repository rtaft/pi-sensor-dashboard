import os
import sensors
from sensors.ds18b20 import DS18B20
from sensor_config import save_config, get_config

class Command:
    def __init__(self):
        self.config = []
        self.sensor_types = [('DS18B20', sensors.ds18b20.lookup)]

    def load(self):
        self.config = get_config()

    def menu(self):
        while True:
            options = [('List', self.list_sensors), ('Add', self.add), 
                       ('Remove', self.remove), ('View', self.view), ('Exit', exit)]
            print('Menu')
            for i in range(len(options)):
                print('{}) {}'.format(i+1, options[i][0]))
            selection = int(input('Selection Option: '))
            options[selection-1][1]()

    def list_sensors(self):
        options = [('Edit', self.edit), ('Remove', self.remove), ('View', self.view), ('Back', None)]
        if self.config:
            while True:
                sensor_config = self.select_sensor()
                if sensor_config:
                    print('Select Option:')
                    for i in range(len(options)):
                        print('{}) {}'.format(i+1, options[i][0]))
                    selection = int(input('Selection: '))
                    if options[selection-1][1]:
                        options[selection-1][1](sensor_config)
                    else:
                        break
                else:
                    break
        else:
            print('No Sensors Found')

    def select_sensor(self):
        print('Select Sensor:')
        for i in range(len(self.config)):
            print('{}) {}: {}'.format(i+1, self.config[i]['sensor_type'].split('.')[-1], self.config[i]['name']))
        print('{}) Back'.format(len(self.config) + 1))
        selection = int(input('Selection: '))
        if selection <= len(self.config):
            return self.config[selection-1]
        return None

    def edit(self, sensor_config):
        name = input('New Name: ')
        sensor_config['name'] = name
        save_config(self.config)

    def add(self):
        print('Sensor Type: ')
        for i in range(len(self.sensor_types)):
            print('{}) {}'.format(i+1, self.sensor_types[i][0]))
        print('{}) Back'.format(len(self.sensor_types) + 1))
        selection = int(input('Selection: '))
        if selection <= len(self.sensor_types):
            sensor_config = self.sensor_types[selection-1][1](self.config)
            self.config.append(sensor_config)
            save_config(self.config)

    def remove(self, sensor_config=None):
        if not sensor_config:
            sensor_config = self.select_sensor()
        if sensor_config:
            self.config.remove(sensor_config)
            save_config(self.config)

    def view(self, sensor_config=None):
        if not sensor_config:
            sensor_config = self.select_sensor()
        if sensor_config:
            sensor_class = self.get_class(sensor_config['sensor_type'])
            sensor = sensor_class()
            sensor.set_config(sensor_config)
            print('{} {}'.format(sensor.get_value(), sensor.get_units()))

    def get_class( self,  kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m 

if __name__== "__main__":
    command = Command()
    command.load()
    command.menu()
