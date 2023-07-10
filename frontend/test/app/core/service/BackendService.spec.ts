import {HttpClientTestingModule, HttpTestingController,} from '@angular/common/http/testing';
import {BackendService} from "../../../../src/app/core/service/BackendService";
import {TestBed} from "@angular/core/testing";
import {ProjectMother} from "../model/ProjectMother";

describe('BooksService', () => {
  let service: BackendService;
  let httpController: HttpTestingController;
  let url = 'http://localhost:8000';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
    });
    service = TestBed.inject(BackendService);
    httpController = TestBed.inject(HttpTestingController);
  });

  it('should POST /projects and return empty body', () => {
    const project = ProjectMother.create()
    service.addProject(project).subscribe(value => {
      console.log(value)
    })

    const req = httpController.expectOne({
      method: 'POST',
      url: `${url}/projects`,
    });

    req.flush(project);
  });

  it('deleteProject should DELETE /projects/id and return empty body', () => {
    const project = ProjectMother.create()
    service.deleteProject("123").subscribe(value => {
      console.log(value)
    })

    const req = httpController.expectOne({
      method: 'DELETE',
      url: `${url}/projects/123`,
    });

    req.flush(project);
  });
});
