#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class"""
        if kwargs and kwargs is not None:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.\
                        strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.\
                        strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
