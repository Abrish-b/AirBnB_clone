#!/usr/bin/python3
"""Defines a base class module"""
from datetime import datetime
import uuid


class BaseModel():
    """this is base class parent class which contain
       id, created at and updated at    
    """

    def __init__(self, *args, **kwargs):
        """initialize a BaseClass with public instances"""
        if kwargs != {}:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                elif key == "__class__":
                    pass
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update Updated at when it's instances are being updated."""
        self.updated_at = datetime.now()

    def to_dict(self):
        data = {}
        for key in self.__dict__:
            if key == 'created_at' or key == 'updated_at':
                data[key] = self.__dict__[key].isoformat()
            else:
                data[key] = self.__dict__[key]
        data["__class__"] = self.__class__.__name__
        return data

    def __str__(self):
        """Define the Printable representation of BaseClass."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
