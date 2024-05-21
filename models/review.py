#!/usr/bin/python3
"""The `review` module.

It defines one class, `Review`,
which sub-classes the `BaseModel` class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text (str): The text of the review.
        user_id (str): The ID of the user who posted the review.
        place_id (str): The ID of the place being reviewed.
    """
    text: str = ""
    user_id: str = ""
    place_id: str = ""
