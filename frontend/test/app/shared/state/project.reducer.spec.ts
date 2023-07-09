import {fetchAllProjects, fetched} from "../../../../src/app/shared/state/project.action";
import {initialState, reducer} from "../../../../src/app/shared/state/project.reducer";
import {ProjectMother} from "../../core/model/ProjectMother";

describe("Project reducer", () => {

  it('fetchAllProject should set isLoading to true', () => {
    const state = reducer(initialState, fetchAllProjects)

    expect(state.isLoading).toBeTruthy()
  });

  it('fetched should set isLoading to false', () => {
    const action = fetched({projects: []})

    const state = reducer(initialState, action)

    expect(state.isLoading).toBeFalsy()
  });

  it('fetched should set project from payload', () => {
    const projects = ProjectMother.create();
    const action = fetched({projects: [projects]})

    const state = reducer(initialState, action)

    expect(state.projects.length).toEqual(1)
    expect(state.projects).toEqual([projects])
  });
});
