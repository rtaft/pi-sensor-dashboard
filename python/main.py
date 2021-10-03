import sensor_config
from sensors.mcp3008 import AnalogSensor, MCP3008
from sensors.file_based import FileBasedSensor
from sensors.ds18b20 import DS18B20

def main():
    fileTest()

def fileTest():
    sensor = FileBasedSensor('sensor.txt', 't=([\d*])')
    sensor.get_value()

def mcp3008test():
    # MCP3008 Test
    mcp3008 = MCP3008(id_=1, name='Analog/Digital Converter', spi_device=1, spi_port=0)
    mcp3008.add_sensor(4, AnalogSensor(2, 'Light Sensor', '', 1, 0))
    mcp3008.add_sensor(1, AnalogSensor(3, 'Broken Light Sensor', '', 1, 0))
    mcp3008.add_sensor(7, AnalogSensor(4, 'Thermasistor', 'C', .25, 0))
    sensor_config.save_config(mcp3008.get_config())

if __name__ == "__main__": 
    sensor = DS18B20('sensor.txt')
    print(sensor.get_config())
    sensor2 = DS18B20()
    sensor2.set_config(sensor.get_config())
    print('{} {}'.format(sensor2.get_value(), sensor2.get_units()))

    #    main()