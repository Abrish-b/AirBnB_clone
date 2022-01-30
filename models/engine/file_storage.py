#!/usr/bin/python3
"""class file storage creates a file with JSON representation of BaseModel
"""

import json


class FileStorage():
    """Filestoarge class has a class dict representation in file.json
    """

    def __init__(self):
        self.__file_path = '../'
        self.__objects = {}

    @property
    def all(self):
        return self.__objects.__dict__

    @objects.getter
    def new(self, obj):
        key = str()
        for keys in obj:
            if keys == '__class__':
                key += obj[keys]
                key += '.'
            elif keys == 'id':
                key += obj[keys]
        self.__objects[key] = obj

    def save(self):
        my_str = json.dumps(self.__objects)
        json_file = open(self.__file_path+"file.json", "w")
        json_file.write(my_str)
        json_file.close()

    def reload(self):
        f = open(self.__file_path+"file.json", "r")
        f.read()
