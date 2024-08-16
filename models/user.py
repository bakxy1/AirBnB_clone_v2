#!/usr/bin/python3
"""Module defines Class `User`"""

from .base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship(
        "Place", back_populates="user", cascade="all, delete, delete-orphan"
    )
