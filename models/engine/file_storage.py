#!/usr/bin/python3
"""This module file_storage define a single class FileStorage
"""

import json
import os.path


class FileStorage:
    """class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    Attributes:
        __file_path (str): (class attribute) path to the JSON file
        __objects (dict): (class attributes) empty but will store
        all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        Returns:
            dict: __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): the obj to save or update in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(data, fp)

    def reload(self):
        """deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists; otherwise, do nothing.
        """
        data = {}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fp:
                data = json.load(fp)
            FileStorage.__objects.clear()
            if data:
                import models.interface
                for key, value in data.items():
                    cls = getattr(models.interface, value['__class__'])
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance

    def find(self, class_name, obj_id):
        """find an object by clas_name and id"""
        key = "{}.{}".format(class_name, obj_id)
        if key in FileStorage.__objects:
            return FileStorage.__objects[key]
        else:
            return None

    def destroy(self, class_name, obj_id):
        """destroy an object by classs name and id"""
        key = "{}.{}".format(class_name, obj_id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
            return True
        return False

    def findAll(self):
        """find all objects"""
        ret_val = []
        for key, value in FileStorage.__objects.items():
            ret_val.append(str(value))
        return ret_val

    def findByClassName(self, class_name):
        """find by class name"""
        ret_val = []
        for key, value in FileStorage.__objects.items():
            if class_name == value.__class__.__name__:
                ret_val.append(str(value))
        return ret_val


if __name__ == '__main__':
    storage = FileStorage()
    print(storage.all())
