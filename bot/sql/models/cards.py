from sqlalchemy import Column, Integer, String

from . import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    file = Column(String, nullable=False)
    user = Column(String, nullable=False)
