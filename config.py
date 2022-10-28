import os
import yaml
from error import ConfigNotFoundException


def load_config(config_file: str):
    if not os.path.exists(config_file):
        config_file = "config.yaml.example"

    with open(config_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError:
            raise ConfigNotFoundException

