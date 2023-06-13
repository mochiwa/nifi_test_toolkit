from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from src.app.domain.testcase.project import Project
from src.app.domain.testcase.project_repository import ProjectRepository
from src.app.infrastructure.persistence.sql.entity.project_model import ProjectModel


class SQlProjectRepository(ProjectRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_project(self, project_id: str):
        with self.session_factory() as session:
            model = session.query(ProjectModel).get(project_id)
            return ProjectModel.to_domain(model)

    def save(self, project: Project):
        with self.session_factory() as session:
            model = ProjectModel.from_domain(project)
            output = session.merge(model)
            session.commit()
            return output
