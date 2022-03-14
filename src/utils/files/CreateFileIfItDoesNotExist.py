from os.path import isfile


def create_file_if_it_does_not_exist(path):
    if not isfile(path):
        open(path, "x")
