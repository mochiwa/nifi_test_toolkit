import {Project} from "../../../../src/app/core/model/Project";


export class ProjectMother {

  public static create(data={
           project_name : 'project name',
           project_uri : 'http://localhost',
           authentication : true,
           username : 'root',
           password : 'root'
         }): Project {
    return {
      project_name : data.project_name,
      project_uri : data.project_uri,
      authentication : data.authentication,
      username : data.username,
      password : data.password
    }
  }
}
