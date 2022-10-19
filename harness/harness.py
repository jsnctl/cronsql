import random
import time

from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import Column, DateTime, func, Integer, Float, create_engine

Base = declarative_base()


class Example(Base):
    __tablename__ = "example"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=func.now())
    value_a = Column(Integer)
    value_b = Column(Float)



def write_to_test_database(s: Session):
    example = Example(
        value_a=random.randint(0, 10),
        value_b=random.random()
    )

    s.add(example)
    s.commit()


engine = create_engine("postgresql://postgres:postgres@database:5432/postgres")
session = sessionmaker(bind=engine)()
Base.metadata.create_all(engine)

while True:
    write_to_test_database(session)
    time.sleep(3)
