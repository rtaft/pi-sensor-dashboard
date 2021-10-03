import flask
from flask import request
import flask_restful as restful
from marshmallow import Schema, fields, validate

from api.helpers import success, created
from api.exceptions import NotFound
from api.restful import API

class Reading (restful.Resource):
    def __init__(self, *args, **kwargs):
        self.sensor_service = kwargs['sensor_service']
    #TODO base class

    def get(self, sensor_id):
        print(sensor_id)
        return success(self.sensor_service.get_reading(sensor_id))