#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
