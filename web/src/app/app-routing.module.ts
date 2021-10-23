import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent } from './dashboard/dashboard.component';
import { AddSensorComponent } from './sensor-management/add-sensor/add-sensor.component';
import { SensorManagementComponent } from './sensor-management/sensor-management.component';
import { ViewSensorComponent } from './sensor-management/view-sensor/view-sensor.component';

const routes: Routes = [ 
  { path: '', component: DashboardComponent },
  { path: 'sensor-management', component: SensorManagementComponent },
  { path: 'sensor-management/new', component: AddSensorComponent },
  { path: 'sensor-management/:id', component: ViewSensorComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
