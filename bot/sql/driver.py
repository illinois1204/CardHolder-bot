import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

engine = create_engine(
    f"sqlite:///{os.getcwd()}/storage/dataBase.db",
    connect_args={"check_same_thread": False},
)

Base.metadata.create_all(bind=engine)
sql = sessionmaker(autoflush=False, bind=engine)()
