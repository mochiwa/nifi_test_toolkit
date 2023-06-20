from app.application.request.create_project_request import CreateProjectRequest


class CreateProjectRequestMother:

    @classmethod
    def payload(cls,
                project_name="project_name",
                project_uri="http://localhost:8080",
                authentication=True,
                username="username",
                password="password") -> dict:
        return {
            "project_name": project_name,
            "project_uri": project_uri,
            "authentication": authentication,
            "username": username,
            "password": password,
        }

    @classmethod
    def create(cls,
               project_name="project_name",
               project_uri="http://localhost:8080",
               authentication=True,
               username="username",
               password="password"
               ) -> CreateProjectRequest:
        data = cls.payload(project_name, project_uri, authentication, username, password)
        return CreateProjectRequest.create(data)
