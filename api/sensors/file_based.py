import re
from sensors.sensor import Sensor, SensorSchema
from marshmallow import fields

class FileBasedSchema(SensorSchema):
    path = fields.String(required=True, allow_none=False, metadata=dict(fieldname="Path", notes="Path to sensor readings file."))
    regexp = fields.String(required=False, allow_none=True, metadata=dict(fieldname="Regexp", notes="Regular Expression for parsing the file"))
    factor = fields.Float(required=False, allow_none=True, metadata=dict(fieldname="Factor", notes="Multiple value by this number to get actual value."))

class FileBasedSensor(Sensor):
    def __init__(self, units=None, name=None, path=None, regexp=None, factor=None):
        Sensor.__init__(self, name=name, units=units)
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

