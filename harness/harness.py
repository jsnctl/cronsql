import random
import time

from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import Column, Time, func, Integer, Float, create_engine
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Example(Base):
    __tablename__ = "example"
    row_id = Column(UUID(as_uuid=True), primary_key=True, unique=True)
    timestamp = Column(Time, default=func.now())
    value_a = Column(Integer)
    value_b = Column(Float)



def write_to_test_database(session: Session):
    example = Example(
        value_a=random.randint(0, 10),
        value_b=random.random()
    )

    session.add(example)
    session.commit()


engine = create_engine("postgresql://postgres:postgres@database:5432")
Session = sessionmaker(bind=engine)
session = Session()

while True:
    write_to_test_database(session)
    time.sleep(3)
