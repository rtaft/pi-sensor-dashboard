import { ChangeDetectorRef, Component, Input, OnDestroy, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-file-based',
  templateUrl: './file-based.component.html',
  styleUrls: ['./file-based.component.scss', '../add-sensor.component.scss']
})
export class FileBasedComponent implements OnInit, OnDestroy {
  @Input() formGroup: FormGroup;
  formControl = new FormControl('', [Validators.required, Validators.pattern("'^(/)([^/\0]+(/)?)+$'")]);

  constructor(private ref: ChangeDetectorRef) { }

  ngOnInit(): void {
    this.formGroup.addControl('path', this.formControl)
  }
  
  ngOnDestroy() {
    this.formGroup.removeControl('path');
  }
}
