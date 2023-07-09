import {ProjectEffect} from "../../../../src/app/shared/state/project.effect";
import {BackendService} from "../../../../src/app/core/service/BackendService";
import {BackendServiceMock} from "../../../helper/mock/BackendServiceMock";
import {TestBed} from "@angular/core/testing";
import {provideMockActions} from "@ngrx/effects/testing";
import {Observable, of} from "rxjs";
import {MockStore, provideMockStore} from "@ngrx/store/testing";
import {AppState} from "../../../../src/app/shared/state/project.state";
import {fetchAllProjects, fetched} from "../../../../src/app/shared/state/project.action";
import {ProjectMother} from "../../core/model/ProjectMother";
import {HttpMother} from "../../../helper/mother/HttpMother";
import {initialState} from "../../../../src/app/shared/state/project.reducer";

describe("State Project effect", () => {
  let actions$: Observable<any>;
  let effects: ProjectEffect;
  let store: MockStore<AppState>;
  let backend: BackendService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ProjectEffect,
        provideMockActions(() => actions$),
        provideMockStore({initialState}),
        {
          provide: BackendService,
          useClass: BackendServiceMock
        }
      ],
    });
    effects = TestBed.inject(ProjectEffect);
    store = TestBed.inject(MockStore);
    backend = TestBed.inject(BackendService);
  });

  describe("GetAll", () => {
    const projects = [ProjectMother.create()];
    const httpResponse = HttpMother.default({code: 200}, projects);

    it('should call backend#getAll', (done) => {
      const spy = spyOn(backend, 'getAll').and.returnValue(of(httpResponse));
      actions$ = of(fetchAllProjects);
      effects.getAll$.subscribe((res) => {
        expect(res).toEqual(fetched({
          projects: projects
        }));
        expect(spy).toHaveBeenCalled();
        done();
      });
    });
  });

})
