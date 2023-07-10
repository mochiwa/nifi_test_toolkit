import {Observable} from "rxjs";

export class BackendServiceMock {
  public addProject(project: {}) {

  }

  public getAll() {
    return new Observable()
  }
  public deleteProject() {
    return new Observable()
  }
}
