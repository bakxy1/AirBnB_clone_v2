#!/usr/bin/python3
"""Module defines `State` class"""

from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    from models import storage_t

    if storage_t == "db":
        cities = relationship(
            "City", back_populates="state", cascade="all, delete, delete-orphan"
        )
    else:

        @property
        def cities(self):
            """Return cities in State"""
            from models import storage

            state_cities = []

            for _, v in storage.all():
                if v.__class__.__name__ == "City" and v.state_id == self.id:
                    state_cities.append(v)

            return state_cities
