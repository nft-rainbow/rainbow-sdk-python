# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GormDeletedAt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time: str=None, valid: bool=None):
        """GormDeletedAt - a model defined in OpenAPI

        :param time: The time of this GormDeletedAt.
        :param valid: The valid of this GormDeletedAt.
        """
        self.openapi_types = {
            'time': str,
            'valid': bool
        }

        self.attribute_map = {
            'time': 'time',
            'valid': 'valid'
        }

        self._time = time
        self._valid = valid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GormDeletedAt':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The gorm.DeletedAt of this GormDeletedAt.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time(self):
        """Gets the time of this GormDeletedAt.


        :return: The time of this GormDeletedAt.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GormDeletedAt.


        :param time: The time of this GormDeletedAt.
        :type time: str
        """

        self._time = time

    @property
    def valid(self):
        """Gets the valid of this GormDeletedAt.

        Valid is true if Time is not NULL

        :return: The valid of this GormDeletedAt.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this GormDeletedAt.

        Valid is true if Time is not NULL

        :param valid: The valid of this GormDeletedAt.
        :type valid: bool
        """

        self._valid = valid
