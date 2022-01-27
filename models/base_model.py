#!/usr/bin/python3
"""Defines a base class module"""
from datetime import datetime
import uuid


class BaseModel():
    """this is base class parent class which contain
       id, created at and updated at    
    """

    def __init__(self):
        """initialize a BaseClass with public instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update Updated at when it's instances are being updated."""
        self.updated_at = datetime.now()

    def to_dict(self):
        data = {}
        for key in self.__dict__:
            if key == 'created_at':
                data[key] = self.__dict__[key].isoformat()
            elif key == 'updated_at':
                data[key] = self.__dict__[key].isoformat()
            else:
                data[key] = self.__dict__[key]
        data["__class__"] = self.__class__.__name__
        return data

    def __str__(self):
        """Define the Printable representation of BaseClass."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
