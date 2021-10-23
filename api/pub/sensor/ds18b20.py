import flask
from flask import request
import flask_restful as restful
from marshmallow import Schema, fields, validate

from api.helpers import success, created
from api.exceptions import NotFound
from sensors.ds18b20 import lookup

class DS18B20Query (restful.Resource):
    def __init__(self, *args, **kwargs):
        self.sensor_service = kwargs['sensor_service']

    def get(self):
        available = lookup(self.sensor_service.get_config())
        return success(available)

