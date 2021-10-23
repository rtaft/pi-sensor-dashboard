import flask_restful as restful
from marshmallow_jsonschema import JSONSchema
from sensors.ds18b20 import DS18B20Schema
from sensors.file_based import FileBasedSchema


class SensorSchema (restful.Resource):
    def get(self):
        sensor_schemas = {"DS18B20": DS18B20Schema(), 
                          "FileBased": FileBasedSchema()}
        json_schemas = {}

        for schema in sensor_schemas:
            json_schemas.append(list(JSONSchema().dump(schema)['definitions'].values())[0]['properties'])

        return json_schemas
