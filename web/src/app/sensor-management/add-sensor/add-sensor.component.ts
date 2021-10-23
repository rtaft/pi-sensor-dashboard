import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-add-sensor',
  templateUrl: './add-sensor.component.html',
  styleUrls: ['./add-sensor.component.scss'],
})
export class AddSensorComponent implements OnInit {
  availableSensors: any;
  availableSensorsMap = {'sensors.ds18b20.DS18B20': 'DS18B20',
                         'sensors.file_based.FileBasedSensor': "File Based"}
  sensorType: string;
  sensorConfig: any;
  formGroup: FormGroup;


  constructor() {}


  ngOnInit(): void {
    this.sensorConfig = {}
    this.formGroup = new FormGroup({
      name: new FormControl('', [Validators.required, Validators.maxLength(255)]),
      sensor_type: new FormControl('', [Validators.required])
    });
    this.formGroup.valueChanges.subscribe(model => {
      this.sensorType = model.sensor_type;
      this.sensorConfig = model;
      console.log(this.sensorConfig)
    })
    this.availableSensors = Object.keys(this.availableSensorsMap);
  }

  submit() {
    if (!this.formGroup.valid) {
      this.formGroup.markAllAsTouched();
    }
    console.log(this.sensorConfig);
    console.log(this.formGroup.valid)
  }
}
