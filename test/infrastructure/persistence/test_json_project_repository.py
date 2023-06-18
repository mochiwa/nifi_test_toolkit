import os
import shutil
import uuid

import pytest

from app.domain.project.project import Project
from app.infrastructure.persistence.json_project_repository import JsonProjectRepository, ROOT_DIR_NAME

repository = JsonProjectRepository()
project = Project(project_id=str(uuid.uuid4()))


@pytest.fixture(autouse=True)
def setup():
    yield
    shutil.rmtree(f"./{ROOT_DIR_NAME}")


def test_save_should_create_project_id_directory():
    repository.save(project)

    assert os.path.isdir(f"./{ROOT_DIR_NAME}/{project.project_id}")


def test_save_should_create_file_project_json_in_project_id_directory():
    repository.save(project)

    assert os.path.isfile(f"./{ROOT_DIR_NAME}/{project.project_id}/project.json")


def test_get_should_return_existing_project():
    repository.save(project)

    found = repository.get(project.project_id)

    assert found is not None
    assert found.project_id == project.project_id
