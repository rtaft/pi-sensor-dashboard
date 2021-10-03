import re
from sensors.sensor import Sensor

class FileBasedSensor(Sensor):
    def __init__(self, id_=None, units=None, name=None, path=None, regexp=None, factor=None):
        Sensor.__init__(self, id_=id_, name=name, units=units)
        self.path = path
        self.regexp = regexp
        self.factor = factor
        self.sensor_type = 'sensors.file_based.FileBasedSensor'
    
    def get_config(self):
        return dict(self.__dict__)
    
    def set_config(self, config):
        self.__dict__.update(config)
    
    def get_raw_value(self):
        with open(self.path, 'r') as fp:
            data = fp.read()
            match = re.search(self.regexp, data)
            return float(match.groups()[0])

    def get_value(self):
        return self.get_raw_value() * self.factor

