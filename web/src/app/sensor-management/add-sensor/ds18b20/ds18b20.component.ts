import { AfterContentInit, Component, Input, OnInit, OnDestroy } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { LookupService } from 'src/app/services/lookup';

@Component({
  selector: 'app-ds18b20',
  templateUrl: './ds18b20.component.html',
  styleUrls: ['./ds18b20.component.scss', '../add-sensor.component.scss']
})
export class Ds18b20Component implements OnInit, AfterContentInit, OnDestroy {
  available: string[] = [];
  @Input() formGroup: FormGroup;
  @Input() formControl = new FormControl('', [Validators.required])

  constructor(private lookupService: LookupService) { }

  async ngOnInit(): Promise<void> {
    this.available = await this.lookupService.getDS18B20().toPromise();
  }

  ngAfterContentInit() {
    this.formGroup.addControl('device', this.formControl)
  }

  ngOnDestroy() {
    this.formGroup.removeControl('device');
  }
}
