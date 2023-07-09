import json
import os
import shutil
from types import SimpleNamespace

from app.domain.project.project import Project
from app.domain.project.project_repository import ProjectRepository

ROOT_DIR_NAME = 'nttk'
PROJECT_FILE_NAME = "project.json"


class JsonProjectRepository(ProjectRepository):

    def __init__(self, root_dir: str = "./"):
        self._root_dir = os.path.join(root_dir, ROOT_DIR_NAME)
        os.makedirs(self._root_dir, exist_ok=True)

    def save(self, project: Project) -> Project:
        self._merge(project)
        return project

    def get(self, project_id: str) -> Project:
        path = os.path.join(self._root_dir, project_id, PROJECT_FILE_NAME)
        return self._file_to_model(path)

    def get_all(self) -> [Project]:
        data = []
        for project_id in os.listdir(self._root_dir):
            data.append(self.get(project_id))
        return data

    def delete_project(self, project_id: str):
        project_path = f"{self._root_dir}/{project_id}"
        if os.path.exists(project_path):
            shutil.rmtree(project_path)

    def _file_to_model(self, path: str) -> Project:
        with open(path, 'r') as file:
            return json.loads(file.read(), object_hook=lambda x: SimpleNamespace(**x))

    def _create_directory(self, directory_name: str):
        path = os.path.join(self._root_dir, directory_name)
        os.makedirs(path, exist_ok=True)
        return path

    def _merge(self, project: Project):
        path = self._create_directory(project.project_id)
        with open(os.path.join(path, PROJECT_FILE_NAME), 'w') as file:
            file.write(json.dumps(project.__dict__))
