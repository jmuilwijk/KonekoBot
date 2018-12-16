from sqlalchemy import (
    Column,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import INTEGER


db_uri = 'sqlite:///src/core/data/currency.sqlite'
engine = create_engine(db_uri)

Base = declarative_base()


class Currency(Base):
    __tablename__ = 'currency'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(INTEGER, nullable=False, primary_key=True)
    snowflake = Column(INTEGER, nullable=False)
    guild = Column(INTEGER, nullable=False)
    amount = Column(INTEGER, nullable=False)


Base.metadata.create_all(engine)
