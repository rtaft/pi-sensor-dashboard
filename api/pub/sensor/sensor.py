import flask
from flask import request
import flask_restful as restful
from marshmallow import Schema, fields, validate

from api.helpers import success, created
from api.exceptions import NotFound
#from api.restful import API

#@API.route('/sensors', methods=['GET'], resource_class_kwargs={'test': 'foo'})
class SensorsConfig (restful.Resource):
    def __init__(self, *args, **kwargs):
        self.sensor_service = kwargs['sensor_service']


    # def get(self):
    #     return success(self.sensor_service.get_sensor_ids()) 

    def get(self):
        return success(self.sensor_service.get_config())

    def post(self):
        data = request.get_json(force=True)
        # TODO validator?
        sensor_id = self.sensor_service.set_config(None, data)
        return success(sensor_id)

    def put(self, sensor_id):
        data = request.get_json(force=True)
        # TODO validator?
        sensor_id = self.sensor_service.set_config(sensor_id, data)
        return success(sensor_id)
    
    def delete(self, sensor_id):
        self.sensor_service.remove_sensor(sensor_id)
        return success()