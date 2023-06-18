class Project:
    def __init__(self, project_id: str):
        self.project_id = project_id

    @property
    def id(self):
        return self.project_id
