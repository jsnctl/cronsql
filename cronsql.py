import pandas as pd
import sqlalchemy.exc
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@database:5432/postgres")


def ping():
    try:
        result = pd.read_sql(f"""
            SELECT * 
            FROM example 
            WHERE timestamp > NOW() - INTERVAL '10 seconds';
        """, engine)
        return result
    except sqlalchemy.exc.OperationalError:
        return None


print(ping())
