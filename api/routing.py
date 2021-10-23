from api.restful import API, APP #, SOCK

import pub.sensor.sensor
import pub.sensor.reading
import pub.sensor.ds18b20

def route(sensor_service):
    kwargs = {'sensor_service': sensor_service}
    API.add_resource(pub.sensor.reading.Reading, '/api/reading/<sensor_id>', methods=['GET'], resource_class_kwargs=kwargs)
    API.add_resource(pub.sensor.sensor.SensorsConfig, '/api/sensors', '/api/sensors/<sensor_id>', methods=['GET', 'POST', 'PUT', 'DELETE'], resource_class_kwargs=kwargs)
    API.add_resource(pub.sensor.ds18b20.DS18B20Query, '/api/lookup/ds18b20', methods=['GET'], resource_class_kwargs=kwargs)
