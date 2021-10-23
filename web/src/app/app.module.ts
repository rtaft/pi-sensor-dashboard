import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MenuComponent } from './menu/menu.component';

//services
import { SensorService } from './services/sensor';
import { LookupService } from './services/lookup';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SensorManagementComponent } from './sensor-management/sensor-management.component';
import { AddSensorComponent } from './sensor-management/add-sensor/add-sensor.component';
import { ViewSensorComponent } from './sensor-management/view-sensor/view-sensor.component';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Ds18b20Component } from './sensor-management/add-sensor/ds18b20/ds18b20.component';
import { FileBasedComponent } from './sensor-management/add-sensor/file-based/file-based.component';


@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    DashboardComponent,
    SensorManagementComponent,
    AddSensorComponent,
    ViewSensorComponent,
    Ds18b20Component,
    FileBasedComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    MatMenuModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    MatSelectModule,
    MatToolbarModule,
    MatTableModule,
    ReactiveFormsModule,
  ],
  providers: [SensorService, LookupService],
  bootstrap: [AppComponent]
})
export class AppModule { }
