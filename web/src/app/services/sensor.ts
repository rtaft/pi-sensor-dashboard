import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Sensor } from '../model/sensor';


@Injectable()
export class SensorService {
    constructor(private httpClient: HttpClient) {}

    getSensorsList(): Observable<Sensor[]> {
        return this.httpClient.get<Sensor[]>('/api/sensors');
    }

    getSensor(sensorId: string): Observable<string> {
        return this.httpClient.get<string>('/api/sensors/' + sensorId);
    }
}