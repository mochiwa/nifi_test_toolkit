import {ProjectPanelComponent} from '../../../../src/app/home/project-panel/project-panel.component';
import {createComponentFactory, Spectator} from "@ngneat/spectator";
import {MatDialog} from "@angular/material/dialog";
import {
  AddProjectFormComponent
} from "../../../../src/app/home/project-panel/add-project-form/add-project-form.component";
import {MatDialogMock} from "../../../helper/mock/modalMock";

describe('ProjectPanelComponent', () => {
  let component: ProjectPanelComponent;
  let view: Spectator<ProjectPanelComponent>;
  const factory = createComponentFactory({
    component: ProjectPanelComponent,
    componentProviders: [{
      provide: MatDialog,
      useClass: MatDialogMock
    }]
  })
  beforeEach(() => {
    view = factory()
    component = view.component
  });

  it('should open add_project-form when click on add_project-btn', () => {
    spyOn(component.addProjectForm, "open");

    expect(view.query('[data-tst="add_project-form"]')).toBeFalsy();

    view.click('[data-tst="add_project-btn"]');

    expect(component.addProjectForm.open).toHaveBeenCalledWith(AddProjectFormComponent);
  });
});
