import { Component } from '@angular/core';
import {MatButtonModule} from "@angular/material/button";
import {MatDialog, MatDialogModule} from "@angular/material/dialog";
import {AddProjectFormComponent} from "./add-project-form/add-project-form.component";

@Component({
  standalone: true,
  selector: 'app-project-panel',
  templateUrl: './project-panel.component.html',
  styleUrls: ['./project-panel.component.css'],
  imports: [
    MatButtonModule,
    MatDialogModule
  ],
})
export class ProjectPanelComponent {

  constructor(public addProjectForm: MatDialog) {
  }

  openAddProjectForm() {
    this.addProjectForm.open(AddProjectFormComponent);
  }
}
