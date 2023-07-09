import {fakeAsync, tick} from '@angular/core/testing';

import {
  AddProjectFormComponent
} from '../../../../../src/app/home/project-panel/add-project-form/add-project-form.component';
import {byRole, byText, byTextContent, createComponentFactory, Spectator} from "@ngneat/spectator";
import {MatDialogRef} from "@angular/material/dialog";
import {MatDialogMock} from "../../../../helper/mock/modalMock";
import {BackendService} from "../../../../../src/app/core/service/BackendService";
import {BackendServiceMock} from "../../../../helper/mock/BackendServiceMock";
import {HttpMother} from "../../../../helper/mother/HttpMother";
import {of, throwError} from "rxjs";

describe('AddProjectFormComponent', () => {
  let component: AddProjectFormComponent;
  let view: Spectator<AddProjectFormComponent>;

  const factory = createComponentFactory({
    component: AddProjectFormComponent,
    componentProviders: [
      {
        provide: MatDialogRef,
        useClass: MatDialogMock
      },
      {
        provide: BackendService,
        useClass: BackendServiceMock
      }
    ]
  })
  beforeEach(() => {
    view = factory()
    component = view.component
  });

  it('should contains the [data-tst="add_project-form"]', () => {
    expect(view.query('[data-tst="add_project-form"]')).toBeTruthy();
    expect(view.query('[data-tst="add_project-form"] form')).toBeTruthy();
  });

  it('should close [data-tst="add_project-form"] when click on cancel', () => {
    spyOn(component.dialogRef, "close");
    view.click(byText('Cancel'));
    expect(component.dialogRef.close).toHaveBeenCalled();
  });

  describe("form validation", () => {
    beforeEach(() => {
      view.typeInElement("my project", 'input[name="project_name"]');
      view.typeInElement("http://localhost:8080", 'input[name="project_uri"]');
      view.click(byRole('checkbox', {checked: false}));
      view.typeInElement("admin", 'input[name="username"]');
      view.typeInElement("password", 'input[name="password"]');
    })

    it('should submit the form when click on submit button', fakeAsync(() => {
      spyOn(component.backendService, "addProject").and.returnValue(of(HttpMother.default({})));
      spyOn(component.dialogRef, "close");
      view.click(byText('Submit'));
      tick()

      expect(component.backendService.addProject).toHaveBeenCalledWith({
        project_id: undefined,
        project_name: "my project",
        project_uri: "http://localhost:8080",
        authentication: true,
        username: "admin",
        password: "password"
      });
      expect(component.dialogRef.close).toHaveBeenCalled();
    }));

    it('should not close the form when backend raise error', fakeAsync(() => {
      spyOn(component.dialogRef, 'close');
      spyOn(component.backendService, "addProject").and.returnValue(throwError(() => HttpMother.error()))

      view.click(byText('Submit'));

      expect(view.query('[data-tst="add_project-form"]')).toBeTruthy();
      expect(component.dialogRef.close).not.toHaveBeenCalled();
    }));


    it('should disable submit button when form is not valid', () => {
      view.typeInElement("", 'input[name="project_name"]');
      expect(view.query(byTextContent('Submit', {selector: 'button'}))).toBeDisabled();
    });
    it('should display error message when project_name is empty', () => {
      view.typeInElement("", 'input[name="project_name"]');

      expect(view.query('mat-error')).toHaveText('Project name is required.');
      expect(component.projectForm.invalid).toBeTruthy();
    });
    it('should disable username and password fields when authentication is unchecked', () => {
      view.click(byRole('checkbox', {checked: true}));

      expect(view.query('input[name="username"]')).toBeDisabled();
      expect(view.query('input[name="password"]')).toBeDisabled();
    });
    it('should display error message when authentication is checked but username and password is empty', () => {
      view.typeInElement("", 'input[name="username"]');
      view.typeInElement("", 'input[name="password"]');

      expect(component.projectForm.invalid).toBeTruthy();
      expect(view.queryAll('mat-error')).toHaveText('Username is required.');
      expect(view.queryAll('mat-error')).toHaveText('Password is required.');
    });
  })
});
