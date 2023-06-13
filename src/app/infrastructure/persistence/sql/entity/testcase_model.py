from sqlalchemy import Column, String, JSON, ForeignKey

from src.app.domain.testcase.testcase import TestCase
from src.app.infrastructure.persistence.sql.database import Base


class TestCaseModel(Base):
    __tablename__ = "testcase"
    testcase_id = Column(String, primary_key=True)
    name = Column(String)
    start = Column(JSON)
    end = Column(JSON)
    steps = Column(JSON)
    project_id = Column(String, ForeignKey("project.project_id"), primary_key=True)

    @classmethod
    def to_domain(cls, model):
        if model is None:
            return None
        return TestCase(
            testcase_id=model.testcase_id,
            name=model.name,
            start=model.start,
            end=model.end,
            steps=model.steps)

    @classmethod
    def from_domain(cls, domain: TestCase):
        return TestCaseModel(
            testcase_id=domain.testcase_id,
            name=domain.name,
            start=domain.start,
            end=domain.end,
            steps=domain.steps)
