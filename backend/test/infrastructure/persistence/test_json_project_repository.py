import os
import shutil

import pytest

from app.infrastructure.persistence.json_project_repository import JsonProjectRepository, ROOT_DIR_NAME
from domain.project_mother import ProjectMother

repository = JsonProjectRepository()
project = ProjectMother.create()


@pytest.fixture(autouse=True)
def setup():
    yield
    if os.path.exists(f"./{ROOT_DIR_NAME}"):
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


def test_get_all_should_return_all_project_existing_in_root_directory():
    repository.save(project)

    found = repository.get_all()

    assert len(found) == 1
    assert found[0].project_id == project.project_id


def test_delete_project_should_delete_existing_project_directory():
    repository.save(project)

    repository.delete_project(project.project_id)

    assert os.path.isfile(f"./{ROOT_DIR_NAME}/{project.project_id}/project.json") is False


def test_delete_project_should_do_nothing_when_project_not_found():
    repository.delete_project("123")

    assert os.path.isfile(f"./{ROOT_DIR_NAME}/123/project.json") is False
