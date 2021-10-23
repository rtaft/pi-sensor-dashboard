import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Sensor } from '../model/sensor';
import { SensorService } from '../services/sensor';

@Component({
  selector: 'app-sensor-management',
  templateUrl: './sensor-management.component.html',
  styleUrls: ['./sensor-management.component.scss']
})
export class SensorManagementComponent implements OnInit {

  sensors: Sensor[] = [];
  displayedColumns: string[] = ['name', 'uuid', 'sensor_type', 'units'];

  constructor(
    private sensorService: SensorService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.sensorService.getSensorsList().toPromise().then((sensors) => {
      this.sensors = sensors;
    });
  }

  select (sensor: Sensor) {
    console.log(sensor);
    this.router.navigate(['/sensor-management/' + sensor.sensor_id]);
  }
}
