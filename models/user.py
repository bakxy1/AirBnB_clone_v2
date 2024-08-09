#!/usr/bin/python3
"""Module defines Class `User`"""

from .base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
