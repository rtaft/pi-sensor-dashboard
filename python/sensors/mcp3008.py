
from sensors.sensor import Sensor

class MCP3008:
    def __init__(self, id_=None, name=None, spi_port=None, spi_device=None, clk=None, miso=None, mosi=None, cs=None):
        self.spi_port = spi_port
        self.spi_device = spi_device
        self.clk = clk
        self.miso = miso
        self.mosi = mosi
        self.cs = cs
        self.id_ = id_
        self.name = name
        self.sensors = [None] * 8
        self.mcp = None
    
    def add_sensor(self, sensor):
        self.sensors[index] = sensor.index
    
    def get_config(self):
        config = dict(id=self.id_, name=self.name)
        if self.spi_port is not None:
            config['spi_port'] = self.spi_port
            config['spi_device'] = self.spi_device
        else:
            config['clk'] = self.clk
            config['miso'] = self.miso
            config['mosi'] = self.mosi
            config['cs'] = self.cs
        config['sensors'] = []
        for sensor in self.sensors:
            if sensor:
                config['sensors'].append(sensor.get_config())
            else:
                config['sensors'].append(None)
        return config
    
    def setup(self):
        import Adafruit_GPIO.SPI as SPI
        import Adafruit_MCP3008
        if self.spi_port is not None:
            self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.spi_port, self.spi_device))
        else:
            self.mcp = Adafruit_MCP3008.MCP3008(clk=self.clk, cs=self.cs, miso=self.miso, mosi=self.mosi)

class AnalogSensor(Sensor):
    def __init__(self, id_=None, name=None, index=None, units=None, slope=None, y_intercept=None):
        Sensor.__init__(self, id_=id_, name=name, units=units)
        self.slope = slope
        self.y_intercept = y_intercept
        self.index = index
        self.mcp = None
    
    def get_config(self):
        config = dict(self.__dict__)
        del config['mcp']
        return config
    
    def set_config(self, config):
        self.__dict__.update(config)

    def setup(self, mcp):
        self.mcp = mcp

    def get_value(self):
        return self.get_raw_value() * self.slope + self.y_intercept
    
    def get_raw_value(self):
        return self.mcp.read_adc(self.index)