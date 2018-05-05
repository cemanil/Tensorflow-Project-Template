import json
from bunch import Bunch
import os


def get_config_from_json(json_file):
    """
    Get the config from a json file.
    :param json_file: Path to json file.
    :return: config(namespace) or config(dictionary)
    """
    # Parse the configurations from the config json file provided.
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)

    # Convert the dictionary to a namespace using bunch lib.
    config = Bunch(config_dict)

    return config, config_dict


def process_config(json_file):
    config, _ = get_config_from_json(json_file)

    config.results_dir = os.path.join(config.results_dir, config.exp_name)

    config.summary_dir = os.path.join(config.results_dir, "summary/")
    config.checkpoint_dir = os.path.join(config.results_dir, "checkpoint/")

    return config

