import {fetchAllProjects, fetched} from "./project.action";
import {createReducer, on} from "@ngrx/store";
import {AppState} from "./project.state";

export const initialState: AppState = {
  isLoading: false,
  projects: [],
  error: null
}

export const reducer = createReducer(
  initialState,
  on(fetchAllProjects, (state) => {
    return {
      ...state,
      isLoading: true
    }
  }),
  on(fetched, (state, action) => {
      return {
        ...state,
        projects: action.projects,
        isLoading: false
      }
    }
  )
)
