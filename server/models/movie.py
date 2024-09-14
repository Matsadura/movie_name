#!/usr/bin/env python3
"""Holds class Movie"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Movie(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'movies'
    name = Column(String(60), nullable=False)
    description = Column(String(512), nullable=True)
    poster = Column(String(512), nullable=True)
    user_movies = relationship("User_Movie",
                               back_populates="movie",
                               cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)
