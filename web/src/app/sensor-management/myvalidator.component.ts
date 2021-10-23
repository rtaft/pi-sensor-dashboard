import { Directive, forwardRef, Input } from '@angular/core';
import { AbstractControl, NG_VALIDATORS, Validator, ValidatorFn } from '@angular/forms';

@Directive({
  selector: '[myvalidator][ngModel],[myvalidator][ngFormControl]',
  providers: [{
    multi: true,
    provide: NG_VALIDATORS, 
    useExisting: forwardRef(() => MyValidator)      
  }]
})
export class MyValidator implements Validator {
  @Input() myvalidator:ValidatorFn; //same name as the selector

  validate(control: AbstractControl) {
    return this.myvalidator(control);
  }
}