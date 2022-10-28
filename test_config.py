import config


def test_load_config():
    c = config.load_config("config.yaml.example")
    assert c is not None


def test_load_config_no_file():
    c = config.load_config("no_config_file.yaml")
    assert c is not None
