from os.path import isfile
from pathlib import Path


def create_file_if_it_does_not_exist(path):
    if not isfile(path):
        create_directory_if_necessary(path)
        create_file(path)


def create_directory_if_necessary(path):
    path_object = Path(path)
    path_object.parent.mkdir(parents=True)


def create_file(path):
    file = open(path, "x")
    file.close()
