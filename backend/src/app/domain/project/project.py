class Project:
    def __init__(self,
                 project_id: str,
                 project_name: str,
                 project_uri: str,
                 authentication: bool,
                 username: str | None,
                 password: str | None):
        self.project_id = project_id
        self.project_name = project_name
        self.project_uri = project_uri
        self.authentication = authentication
        self.username = username
        self.password = password
