import {Injectable} from "@angular/core";
import {Actions, createEffect, ofType} from "@ngrx/effects";
import {BackendService} from "../../core/service/BackendService";
import {addProject, fetchAllProjects, fetched} from "./project.action";
import {map, mergeMap} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProjectEffect {
  getAll$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fetchAllProjects),
      mergeMap(() => this.backendService.getAll().pipe(
          map((response) => fetched({projects: response.body!})),
        )
      )
    )
  );

  addProject$ = createEffect(()=>
    this.actions$.pipe(
      ofType(addProject),
      mergeMap((project) => this.backendService.addProject(project).pipe(
          map((response)=> fetchAllProjects())
          )
        )
    )
  );

  constructor(
    private actions$: Actions,
    private backendService: BackendService
  ) {
  }
}
