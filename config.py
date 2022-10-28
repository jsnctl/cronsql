import os

import yaml

from error import ConfigNotFoundException


def load_config():
    if not os.path.exists("config.yaml"):
        config_file = "config.yaml.example"
    else:
        config_file = "config.yaml"
    with open(config_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise ConfigNotFoundException
    return config
