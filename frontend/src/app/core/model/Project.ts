export interface Project {//todo: refactor
  project_id: string | undefined,
  project_name: string,
  project_uri: string,
  authentication: boolean,
  username: string | undefined,
  password: string | undefined
}
