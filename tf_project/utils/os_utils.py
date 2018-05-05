from shutil import copy2


def copy_file_to_destination(filepath, destination_path):
    copy2(filepath, destination_path)
