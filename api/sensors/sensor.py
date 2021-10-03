import uuid

class Sensor:
    def __init__(self, name=None, units=None):
        self.units = units
        self.id_ = uuid.uuid4().hex
        self.name = name

    def get_id(self):
        return self.id_

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
