export class Sensor {
    sensor_id: string;
    name: string;
    units: string;
    sensor_type: string;
}

export class FileSensor extends Sensor {
    path: string;
    factor: number;
    regexp: string;
}

export class DS18B20 extends FileSensor{

}