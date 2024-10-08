#!/usr/bin/python3
"""Module defines `Place` class"""

from models.base_model import BaseModel, Base
from models import storage, storage_t

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Place class"""

    __tablename__ = "places"

    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0, nullable=False)
    longitude = Column(Float, default=0, nullable=False)
    amenity_ids = []

    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")

    if storage_t == "db":
        reviews = relationship(
            "Review",
            back_populates="place",
            cascade="all, delete, delete-orphan",
        )
    else:

        @property
        def reviews(self):
            """Return cities in State"""
            from models import storage

            place_reviews = []

            for _, v in storage.all():
                if v.__class__.__name__ == "Review" and v.place_id == self.id:
                    place_reviews.append(v)

            return place_reviews
