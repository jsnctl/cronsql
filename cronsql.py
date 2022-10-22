import pandas as pd
import sqlalchemy.exc
from sqlalchemy import create_engine
import yaml

engine = create_engine("postgresql://postgres:postgres@database:5432/postgres")


def load_config():
    config = None
    with open("./config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return config


def ping():
    config = load_config()

    if not config:
        return "error"

    try:
        result = pd.read_sql(config["query"], engine)
        return result
    except sqlalchemy.exc.OperationalError:
        return None


print(ping())
