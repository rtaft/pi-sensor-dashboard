from marshmallow import Schema, fields

class SensorSchema(Schema):
    name = fields.String(required=True, allow_none=False, metadata=dict(fieldname="Name", notes="Name of the sensor."))
    units = fields.String(required=False, allow_none=True, metadata=dict(fieldname="Units", notes="Units the sensor is in."))


class Sensor:
    def __init__(self, sensor_id=None, name=None, units=None):
        self.units = units
        self.sensor_id = sensor_id;
        self.name = name

    def get_sensor_id(self):
        return self.sensor_id

    def get_name(self):
        return self.name

    def get_value(self):
        raise NotImplementedError()
    
    def get_raw_value(self):
        raise NotImplementedError()

    def get_units(self):
        return self.units
    
    def get_config(self):
        raise NotImplementedError()

    def set_config(self, config):
        raise NotImplementedError()

