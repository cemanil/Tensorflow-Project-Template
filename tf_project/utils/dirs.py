import os


def create_dirs(dirs, override=False):
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs:
    :param override: If set to False, program aborts if the directory already exists to avoid overriding.
    :return exit_code: 0:success -1:failed
    """
    if override:
        for dir_ in dirs:
            create_dir(dir_)
    else:
        for dir_ in dirs:
            create_new_dir(dir_)


def create_dir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return 0
    except Exception as err:
        print("Creating directories error: {0}".format(err))
        exit(-1)


def create_new_dir(directory):
    if os.path.exists(directory):
        print("Directory already exists. Aborting to avoid overriding. ")
        exit(-1)
    else:
        os.makedirs(directory)
