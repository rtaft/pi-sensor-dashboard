import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable()
export class LookupService {
    constructor(private httpClient: HttpClient) {}

    getDS18B20(): Observable<string[]> {
        return this.httpClient.get<string[]>('/api/lookup/ds18b20');
    }
}