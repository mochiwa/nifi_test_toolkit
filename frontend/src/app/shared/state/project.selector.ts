import {GlobalState} from "./project.state";

export const projects = (state: GlobalState) => state?.appState?.projects
export const isLoading = (state: GlobalState) => state.appState.isLoading
export const error = (state: GlobalState) => state.appState.error
