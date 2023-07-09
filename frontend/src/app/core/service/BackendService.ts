import {Injectable} from "@angular/core";
import {Observable} from 'rxjs';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {Project} from "../model/Project";

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private url = "http://localhost:8000"
  private header = new HttpHeaders({'Content-Type': 'application/json'})


  constructor(private http: HttpClient) {
  }

  public addProject(project: Project): Observable<HttpResponse<any>> {
    return this.http.post(`${this.url}/projects`, project, {
      headers: this.header,
      observe: 'response'
    })
  }

  public getAll(): Observable<HttpResponse<Project[]>> {
    return this.http.get<[Project]>(`${this.url}/projects`, {
      observe: 'response'
    })
  }
}
