#!/usr/bin/python3
"""File storage module"""
import json
import datetime


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    """Start Database Crude Operations"""

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

        FileStorage.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict, f)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)

    """End Database Crude Operations"""

    def attr_dict(self):
        """Returns a dict of acceptable attributes"""
        attr_dict = {
            "Review":
                    {"place_id": str,
                        "user_id": str,
                        "text": str},
            "Place":
                    {"city_id": str,
                        "user_id": str,
                        "name": str,
                        "description": str,
                        "number_rooms": int,
                        "number_bathrooms": int,
                        "max_guest": int,
                        "price_by_night": int,
                        "latitude": float,
                        "longitude": float,
                        "amenity_ids": list},
            "Amenity":
                    {"name": str},
            "City":
                    {"state_id": str,
                        "name": str},
            "State":
                    {"name": str},
            "User":
                    {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
            "BaseModel":
                    {"id": str,
                        "created_at": datetime.datetime,
                        "updated_at": datetime.datetime}
        }
        return attr_dict

    def classes_dict(self):
        """Returns a dict of classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}
        return classes_dict

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                dict = json.load(f)
                dict = {k: self.classes_dict()[v["__class__"]](**v)
                        for k, v in dict.items()}
                FileStorage.__objects = dict
        except Exception:
            pass
