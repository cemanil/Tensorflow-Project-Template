import os


def create_dirs(dirs):
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs:
    :return exit_code: 0:success -1:failed
    """
    for dir_ in dirs:
        create_dir(dir_)


def create_dir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return 0
    except Exception as err:
        print("Creating directories error: {0}".format(err))
        exit(-1)
