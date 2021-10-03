import getpass
import os
import sensors
from sensors.ds18b20 import DS18B20
from app_config import save_config, get_config, SENSOR_CONFIG_FILE
import database_manager

class Command:
    def __init__(self):
        self.config = []
        self.sensor_types = [('DS18B20', sensors.ds18b20.lookup)]
        self.db_manager = database_manager.DatabaseManager()

    def load(self):
        self.config = get_config(SENSOR_CONFIG_FILE)

    def generic_menu(self, title, options, *args, **kwargs):
        keyed_options = {option[1].upper(): option[2] for option in options}
        keyed_options['X'] = exit
        keyed_options['Q'] = exit
        keyed_options['B'] = None
        while True:
            print('\n')
            print(title)
            for option in options:
                print('{}) {}'.format(option[1].upper(), option[0]))
            if title == 'Menu':
                print('X) Exit')
            else:
                print('B) Back')

            selection = input('Select Option: ').upper()
            try:
                func = keyed_options[selection]
                if func == exit:
                    exit()
                elif func:
                    func(*args, **kwargs)
                else:
                    break
            except KeyError:
                print('{} is not a valid selection'.format(selection))

    def menu(self):
        options = [('Configure Database', 'D', self.setup_database), 
                   ('Configure Sensors', 'S', self.sensor_menu)]
        self.generic_menu('Menu', options)

    def sensor_menu(self):
        options = [('List', 'L', self.list_sensors), ('Add', 'A', self.add), 
                   ('Remove', 'R', self.remove), ('View', 'V', self.view)]
        self.generic_menu('Sensor Menu', options)

    def list_sensors(self):
        options = [('Edit', 'E', self.edit), ('Remove', 'R', self.remove), ('View', 'V', self.view)]
        if self.config:
            while True:
                sensor_config = self.select_sensor()
                if sensor_config:
                    self.generic_menu('Select Option', options, sensor_config)
                else:
                    break
        else:
            print('No Sensors Found')

    def select_sensor(self):
        print('Select Sensor:')
        for i in range(len(self.config)):
            print('{}) {}: {}'.format(i+1, self.config[i]['sensor_type'].split('.')[-1], self.config[i]['name']))
        print('B) Back')
        selection = self.get_selection(len(self.config))
        if selection:
            return self.config[selection]
        return None

    def get_selection(self, size):
        while True:
            selection = input('Selection: ')
            if selection.isdigit():
                if int(selection) <= size:
                    return int(selection)-1
            elif selection.upper() in  ['X', 'Q']:
                exit()
            elif selection.upper() == 'B':
                return None
            print('{} is not a valid selection\n'.format(selection))

    def edit(self, sensor_config):
        name = input('New Name: ')
        sensor_config['name'] = name
        save_config(SENSOR_CONFIG_FILE, self.config)

    def add(self):
        print('Sensor Type: ')
        for i in range(len(self.sensor_types)):
            print('{}) {}'.format(i+1, self.sensor_types[i][0]))
        print('{}) Back'.format(len(self.sensor_types) + 1))
        selection = int(input('Selection: '))
        if selection <= len(self.sensor_types):
            sensor_config = self.sensor_types[selection-1][1](self.config)
            self.config.append(sensor_config)
            save_config(SENSOR_CONFIG_FILE, self.config)

    def remove(self, sensor_config=None):
        if not sensor_config:
            sensor_config = self.select_sensor()
        if sensor_config:
            self.config.remove(sensor_config)
            save_config(SENSOR_CONFIG_FILE, self.config)
            print('Removed {}'.format(sensor_config['name']) )

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

    def setup_database(self):
        print ('\nSelect Database:')
        dbs = self.db_manager.get_available_databases()
        for i in range(len(dbs)):
            print('{}) {}'.format(i+1, dbs[i]))
        selection = self.get_selection(len(dbs))
        if not selection:
            return None
        db = dbs[selection]
        if db == 'sqlite':
            config = dict(filename='sensors.db')
        else:
            config = self.get_db_config()
        try:
            self.db_manager.connect_database(db, **config)
            self.db_manager.save_db_config(db, config)
        except Exception as e:
            print(e)
    
    def get_db_config(self):
        config = dict(
            database=input("Database Name (sensors): ") or "sensors",
            user=input("User: "),
            password=getpass.getpass(),
            host=input("Hostname (localhost): ") or "localhost",
            port=input("Port (default): "),
        )
        if not config['port']:
            del config['port']
        return config

        

if __name__== "__main__":
    command = Command()
    command.load()
    command.menu()
