import {Component, OnInit} from '@angular/core';
import {MatDialogModule, MatDialogRef} from "@angular/material/dialog";
import {MatButtonModule} from "@angular/material/button";
import {BackendService} from "../../../core/service/BackendService";
import {MatInputModule} from "@angular/material/input";
import {FormControl, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {MatCheckboxModule} from "@angular/material/checkbox";
import {HttpErrorResponse} from "@angular/common/http";
import {NgIf} from "@angular/common";
import {Project} from "../../../core/model/Project";

@Component({
  standalone: true,
  selector: 'app-add-project-form',
  templateUrl: './add-project-form.component.html',
  styleUrls: ['./add-project-form.component.css'],
  imports: [
    MatDialogModule,
    MatButtonModule,
    MatInputModule,
    ReactiveFormsModule,
    MatCheckboxModule,
    NgIf
  ],
})
export class AddProjectFormComponent implements OnInit {
  projectForm = new FormGroup({
    project_name: new FormControl('', Validators.required),
    project_uri: new FormControl(''),
    authentication: new FormControl(false),
    username: new FormControl({value: '', disabled: true}, Validators.required),
    password: new FormControl({value: '', disabled: true}, Validators.required),
  });

  constructor(
    public dialogRef: MatDialogRef<AddProjectFormComponent>,
    public backendService: BackendService) {
  }

  ngOnInit(): void {
    this.projectForm.controls.authentication.valueChanges.subscribe(() => {
      this.toggleField(this.projectForm.controls.username);
      this.toggleField(this.projectForm.controls.password);
    });
  }

  cancel() {
    this.dialogRef.close();
  }

  submit() {
    let payload: Project = Object.assign(this.projectForm.value)
    this.backendService.addProject(payload)
      .subscribe({
        next: () => this.cancel(),
        error: (e: HttpErrorResponse) => console.error(e)
      });
  }

  private toggleField(field: FormControl) {
    field.disabled ? field.enable() : field.disable();
    field.setValue('');
  }
}
