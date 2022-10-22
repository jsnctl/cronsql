import pandas as pd
import sqlalchemy.exc
from sqlalchemy import create_engine
import yaml


def load_config():
    config = None
    engine = None
    with open("./config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            host, database, port, user, password = (
                config["host"],
                config["database"],
                config["port"],
                config["user"],
                config["password"]
            )
            engine = create_engine(
                f"postgresql://{user}:{password}@{host}:{port}/{database}"
            )
        except yaml.YAMLError as e:
            print(e)
    return config, engine


def ping():
    config, engine = load_config()

    if not config:
        return "error"

    try:
        result = pd.read_sql(config["query"], engine)
        return result
    except sqlalchemy.exc.OperationalError:
        return None


print(ping())
