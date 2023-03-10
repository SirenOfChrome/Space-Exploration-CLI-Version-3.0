# Remember to regularly run alembic revision --autogenerate -m'<descriptive message>' 
# #and alembic upgrade head to track your modifications to the database and create checkpoints 
# #in case you ever need to roll those modifications back.

from sqlalchemy import Integer
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create engine and sessionmaker
engine = create_engine('sqlite:///space-exploration.db')
Session = sessionmaker(bind=engine)

# declare the model
Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'

    name = Column(String, primary_key=True)
    star_system = Column(String)
    distance = Column(Float)


class Astronomer(Base):
    __tablename__ = 'astronomers'

    name = Column(String, primary_key=True)
    planet = Column(String)
    born = Column(Integer)

class Spaceship(Base):
    __tablename__ = 'spaceships'

    name = Column(String, primary_key=True)
    planet = Column(String)
    number = Column(Float)
    description = Column(String)

# create the table
Base.metadata.create_all(engine)