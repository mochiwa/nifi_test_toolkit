import {Injectable} from "@angular/core";
import {Observable} from 'rxjs';
import {HttpClient, HttpResponse} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private uri = "http://localhost:8000"

  constructor(private http: HttpClient) {
  }


  public addProject(project: {}): Observable<HttpResponse<any>> {
    return this.http.post(`${this.uri}/projects`, project, {observe: 'response'})

  }

}
