import {Component, OnInit} from '@angular/core';
import {MatButtonModule} from "@angular/material/button";
import {MatDialog, MatDialogModule} from "@angular/material/dialog";
import {MatExpansionModule} from "@angular/material/expansion";
import {Project} from "../../core/model/Project";
import {Observable} from "rxjs";
import {CommonModule} from "@angular/common";
import {Store} from "@ngrx/store";
import {deleteProject, fetchAllProjects} from "../../shared/state/project.action";
import {projects} from "../../shared/state/project.selector";
import {GlobalState} from "../../shared/state/project.state";
import {AddProjectFormComponent} from "./add-project-form/add-project-form.component";
import {MatDividerModule} from "@angular/material/divider";

@Component({
  standalone: true,
  selector: 'app-project-panel',
  templateUrl: './project-panel.component.html',
  styleUrls: ['./project-panel.component.css'],
  imports: [
    MatButtonModule,
    MatDialogModule,
    MatExpansionModule,
    CommonModule,
    MatDividerModule,
  ],
})
export class ProjectPanelComponent implements OnInit {
  projects$: Observable<Project[]> = this.store.select(projects)

  constructor(public addProjectForm: MatDialog,
              private store: Store<GlobalState>) {
  }

  openAddProjectForm() {
    this.addProjectForm.open(AddProjectFormComponent);
  }

  deleteProject(project : Project){
    this.store.dispatch(deleteProject({project_id: project.project_id!}))
  }

  ngOnInit(): void {
    this.store.dispatch(fetchAllProjects())
  }
}
