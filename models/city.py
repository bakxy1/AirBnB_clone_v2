#!/usr/bin/python3
"""Module defines `City` class"""

from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class"""

    __tablename__ = "cities"

    name = Column(String(60), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")
    places = relationship(
        "Place", back_populates="city", cascade="all, delete, delete-orphan"
    )
