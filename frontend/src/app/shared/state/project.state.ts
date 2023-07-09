import {Project} from "../../core/model/Project";

export interface GlobalState {
  appState: AppState
}

export interface AppState {
  isLoading: boolean;
  projects: Project[]
  error: string | null;
}
