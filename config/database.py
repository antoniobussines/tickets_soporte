from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


BATABASE_URL ="sqlite:///config/personal.db"

engine = create_engine(BATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()