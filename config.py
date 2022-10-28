import yaml

from error import ConfigNotFoundException


def load_config():
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise ConfigNotFoundException
    return config
