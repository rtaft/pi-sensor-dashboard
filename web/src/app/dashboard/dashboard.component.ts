import { Component, OnInit } from '@angular/core';
import { Sensor } from '../model/sensor';
import { SensorService } from '../services/sensor';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  sensors: Sensor[] = [];
  displayedColumns: string[] = ['name', 'uuid', 'sensor_type', 'units'];
  constructor(private sensorService: SensorService) { }

  ngOnInit(): void {
    this.sensorService.getSensorsList().toPromise().then((sensors) => {
      this.sensors = sensors;
    });
  }

}
