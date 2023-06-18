import json
import os
from types import SimpleNamespace

from app.domain.project.project import Project
from app.domain.project.project_repository import ProjectRepository

ROOT_DIR_NAME = 'nttk'


class JsonProjectRepository(ProjectRepository):

    def __init__(self, root_dir: str = "./"):
        self._root_dir = os.path.join(root_dir, ROOT_DIR_NAME)
        os.makedirs(self._root_dir, exist_ok=True)

    def save(self, project: Project) -> Project:
        self._merge(project)
        return project

    def get(self, project_id: str) -> Project:
        path = os.path.join(self._root_dir, project_id, 'project.json')
        with open(path, 'r') as file:
            return json.loads(file.read(), object_hook=lambda x: SimpleNamespace(**x))

    def _create_directory(self, directory_name: str):
        path = os.path.join(self._root_dir, directory_name)
        os.makedirs(path, exist_ok=True)
        return path

    def _merge(self, project: Project):
        path = self._create_directory(project.project_id)
        with open(os.path.join(path, 'project.json'), 'w') as file:
            file.write(json.dumps(project.__dict__))
