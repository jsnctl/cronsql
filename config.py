import yaml


def load_config():
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return config
