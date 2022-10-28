import pandas as pd
import sqlalchemy.exc
from sqlalchemy import create_engine

from config import load_config

CONFIG_FILE = "config.yaml"


def query():
    config = load_config(CONFIG_FILE)

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


df = query()
print(df)
