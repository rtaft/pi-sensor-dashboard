import sensors
import pika
from sensors.ds18b20 import DS18B20
from app_config import save_config, get_config, SENSOR_CONFIG_FILE
import database_manager
import time
import json


class SensorService:
    def __init__(self):
        self.readings = {}
        self.sensors = {}

    def load_sensors(self):
        self.sensor_config = get_config()
        for config in self.sensor_config:
            sensor = self.create_sensor(config)
            self.sensors[sensor.get_id()] = sensor

    def create_sensor(self, config):
        sensor_class = self.get_class(config['sensor_type'])
        sensor = sensor_class()
        sensor.set_config(config)
        return sensor

    def connect_db(self):
        pass

    def connect_mq(self):
        credentials = pika.PlainCredentials('sensors', 'sensors')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.121', credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='sensor_readings')

    def run_mq_service(self):
        self.load_sensors()
        self.connect_mq()
        while True:
            for sensor in self.sensors.values():
                message = dict(time=time.time(), id=sensor.get_id(), name=sensor.get_name(), value=sensor.get_value(), units=sensor.get_units())
                message_json =  json.dumps(message)
                self.channel.basic_publish(exchange='', routing_key='sensor_readings', body=message_json)
                print('{} {} {} {} {}'.format(time.time(), sensor.get_id(), sensor.get_name(), sensor.get_value(), sensor.get_units()))
            time.sleep(1)
    
    def run_collection_service(self):
        self.load_sensors()
        while True:
            for sensor in list(self.sensors.values()):
                # if its time to poll sensor
                reading = dict(time=time.time(), id=sensor.get_id(), name=sensor.get_name(), value=sensor.get_value(), units=sensor.get_units())
                self.readings[sensor.get_id()] = reading
            time.sleep(1)
    
    def get_reading(self, sensor_id):
        return self.readings[sensor_id]
    
    def get_readings(self):
        return self.readings
    
    def get_config(self, sensor_id=None):
        if sensor_id:
            return self.sensors[sensor_id].get_config()
        config = []
        for sensor in self.sensors.values():
            config.append(sensor.get_config())
        return config

    def set_config(self, sensor_id, config):
        if sensor_id in self.sensors:
            self.sensors[sensor_id].set_config(config)
        else:
            sensor = self.create_sensor(config)
            self.sensors[sensor.get_id()] = sensor
            sensor_id = sensor.get_id()
        save_config(SENSOR_CONFIG_FILE, self.get_config())
        return sensor_id
    
    def get_sensor_ids(self):
        return list(self.sensors.keys())
    
    def remove_sensor(self, sensor_id):
        del self.sensors[sensor_id]
        save_config(SENSOR_CONFIG_FILE, self.get_config())

    def get_class( self,  kls ): #TODO helper utility
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m 

if __name__ == "__main__": 
    service = SensorService()
    service.run_service()