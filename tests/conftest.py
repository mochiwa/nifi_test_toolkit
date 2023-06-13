import os
import shutil


def pytest_configure(config):
    os.makedirs("./tmp", exist_ok=True)


def pytest_unconfigure(config):
    shutil.rmtree("./tmp")
