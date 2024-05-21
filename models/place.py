#!/usr/bin/python3
"""The `place` module

It defines one class, `Place`,
which sub-classes the `BaseModel` class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place/house in the application.

    It represents a place/house uploaded
    by the users of the application.

    Attributes:
        name (str): The name of the place.
        user_id (str): The ID of the user who owns the place.
        city_id (str): The ID of the city where the place is located.
        description (str): A description of the place.
        number_bathrooms (int): The number of bathrooms in the place.
        price_by_night (int): The price per night to stay at the place.
        number_rooms (int): The number of rooms in the place.
        longitude (float): The longitude of the place's location.
        latitude (float): The latitude of the place's location.
        max_guest (int): The maximum number of guests the place can accommodate.
        amenity_ids (list): A list of amenity IDs available at the place.
    """

    name: str = ""
    user_id: str = ""
    city_id: str = ""
    description: str = ""
    number_bathrooms: int = 0
    price_by_night: int = 0
    number_rooms: int = 0
    longitude: float = 0.0
    latitude: float = 0.0
    max_guest: int = 0
    amenity_ids: list = []
