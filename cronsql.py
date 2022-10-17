import pandas as pd
import sqlalchemy.exc
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@test-database:5432")


def ping():
    try:
        pd.read_sql(f"""SELECT 1""", engine)
        return True
    except sqlalchemy.exc.OperationalError:
        return False


print(ping())
