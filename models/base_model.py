#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel class defines common attr/mtds for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructor  - initializes BaseModel instance"""
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
        """Prints a string representation of class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict of all keys/vals of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
