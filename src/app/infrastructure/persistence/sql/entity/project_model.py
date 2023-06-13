from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.app.domain.testcase.project import Project
from src.app.infrastructure.persistence.sql.database import Base
from src.app.infrastructure.persistence.sql.entity.testcase_model import TestCaseModel


class ProjectModel(Base):
    __tablename__ = "project"
    project_id = Column(String, primary_key=True)
    testcases = relationship("TestCaseModel")

    @classmethod
    def to_domain(cls, model):
        if model is None:
            return None
        return Project(
            project_id=model.project_id,
            testcases=[TestCaseModel.to_domain(testcase) for testcase in model.testcases]
        )

    @classmethod
    def from_domain(cls, domain: Project):
        return ProjectModel(
            project_id=domain.project_id,
            testcases=[TestCaseModel.from_domain(testcase) for testcase in domain.testcases]
        )
