import config


def test_load_config():
    c = config.load_config()
    assert c is not None

