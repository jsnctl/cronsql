import pandas as pd
import sqlalchemy.exc
import yaml
from sqlalchemy import create_engine


def load_config():
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return config


def query():
    config = load_config()

    if not config:
        return "error"

    user, password, host, port, database = (
        config["database"]["user"],
        config["database"]["password"],
        config["database"]["host"],
        config["database"]["port"],
        config["database"]["database"]
    )
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

    try:
        result = pd.read_sql(config["query"], engine)
        return result
    except sqlalchemy.exc.OperationalError:
        return None


print(query())
