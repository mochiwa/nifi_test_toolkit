import {createAction, props} from "@ngrx/store";
import {Project} from "../../core/model/Project";

export enum ActionTypes {
  FETCH_ALL = '[Project Component] GetAll',
  FETCHED = '[Project Component] Fetched',
  ADD_PROJECT = '[Project Component] AddProject',
}

export const fetchAllProjects = createAction(ActionTypes.FETCH_ALL)
export const fetched = createAction(ActionTypes.FETCHED, props<{ projects: Project[] }>())
export const addProject = createAction(ActionTypes.ADD_PROJECT, props<Project>())


