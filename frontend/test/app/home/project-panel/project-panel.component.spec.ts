import {ProjectPanelComponent} from '../../../../src/app/home/project-panel/project-panel.component';
import {createComponentFactory, Spectator} from "@ngneat/spectator";
import {
  AddProjectFormComponent
} from "../../../../src/app/home/project-panel/add-project-form/add-project-form.component";
import {ProjectMother} from "../../core/model/ProjectMother";
import {MockStore, provideMockStore} from "@ngrx/store/testing";
import {initialState} from "../../../../src/app/shared/state/project.reducer";
import {GlobalState} from "../../../../src/app/shared/state/project.state";
import {fakeAsync} from "@angular/core/testing";
import {projects} from "../../../../src/app/shared/state/project.selector";
import {deleteProject} from "../../../../src/app/shared/state/project.action";

describe('ProjectPanelComponent', () => {
  let component: ProjectPanelComponent;
  let view: Spectator<ProjectPanelComponent>;
  let store: MockStore<GlobalState>;
  const factory = createComponentFactory({
    component: ProjectPanelComponent,
    providers: [
      provideMockStore({initialState}),
    ]
  })

  beforeEach(() => {
    view = factory()
    component = view.component
    store = view.inject(MockStore)
  });

  it('should open add_project-form when click on add_project-btn', fakeAsync(() => {
    spyOn(component.addProjectForm, "open");

    view.click('[data-tst="add_project-btn"]');

    expect(component.addProjectForm.open).toHaveBeenCalledWith(AddProjectFormComponent);
    //how to test modal has been open ?
  }));

  it('should get all projects from store when component init', fakeAsync(() => {
    const projects = [ProjectMother.create()]
    const dispatchSpy = spyOn(store, 'dispatch').and.callThrough();

    store.setState({appState: {...initialState, projects: projects}})
    component.ngOnInit()

    component.projects$.subscribe(value => {
      expect(value.length).toEqual(1)
      expect(value[0].project_id).toEqual(projects[0].project_id)
    })
    view.detectChanges()
    expect(view.query('[id="project-panel-123"]')).toBeTruthy()
    expect(dispatchSpy).toHaveBeenCalled()
  }));

  describe("delete project",()=>{
    const project = ProjectMother.create()
    beforeEach(()=>{
      store.setState({appState: {...initialState, projects: [project]}})
      component.ngOnInit()
      view.detectChanges()
    })

    it('should delete project when click on delete button of the the expansion panel', ()=> {
      const dispatchSpy = spyOn(store, 'dispatch').and.callThrough();

      view.click('[id="project-panel-123"] button')
      store.setState({appState: {...initialState, projects: []}})
      view.detectChanges()

      expect(dispatchSpy).toHaveBeenCalledWith(deleteProject({project_id:'123'}))
      expect(view.query('[id="project-panel-123"]')).toBeFalsy()
    });
  })
});
