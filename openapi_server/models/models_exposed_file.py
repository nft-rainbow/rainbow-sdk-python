# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.gorm_deleted_at import GormDeletedAt
from openapi_server import util


class ModelsExposedFile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: str=None, deleted_at: GormDeletedAt=None, file_name: str=None, file_size: int=None, file_type: str=None, file_url: str=None, id: int=None, updated_at: str=None):
        """ModelsExposedFile - a model defined in OpenAPI

        :param created_at: The created_at of this ModelsExposedFile.
        :param deleted_at: The deleted_at of this ModelsExposedFile.
        :param file_name: The file_name of this ModelsExposedFile.
        :param file_size: The file_size of this ModelsExposedFile.
        :param file_type: The file_type of this ModelsExposedFile.
        :param file_url: The file_url of this ModelsExposedFile.
        :param id: The id of this ModelsExposedFile.
        :param updated_at: The updated_at of this ModelsExposedFile.
        """
        self.openapi_types = {
            'created_at': str,
            'deleted_at': GormDeletedAt,
            'file_name': str,
            'file_size': int,
            'file_type': str,
            'file_url': str,
            'id': int,
            'updated_at': str
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'deleted_at': 'deleted_at',
            'file_name': 'file_name',
            'file_size': 'file_size',
            'file_type': 'file_type',
            'file_url': 'file_url',
            'id': 'id',
            'updated_at': 'updated_at'
        }

        self._created_at = created_at
        self._deleted_at = deleted_at
        self._file_name = file_name
        self._file_size = file_size
        self._file_type = file_type
        self._file_url = file_url
        self._id = id
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelsExposedFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The models.ExposedFile of this ModelsExposedFile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this ModelsExposedFile.


        :return: The created_at of this ModelsExposedFile.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsExposedFile.


        :param created_at: The created_at of this ModelsExposedFile.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsExposedFile.


        :return: The deleted_at of this ModelsExposedFile.
        :rtype: GormDeletedAt
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsExposedFile.


        :param deleted_at: The deleted_at of this ModelsExposedFile.
        :type deleted_at: GormDeletedAt
        """

        self._deleted_at = deleted_at

    @property
    def file_name(self):
        """Gets the file_name of this ModelsExposedFile.


        :return: The file_name of this ModelsExposedFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ModelsExposedFile.


        :param file_name: The file_name of this ModelsExposedFile.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this ModelsExposedFile.


        :return: The file_size of this ModelsExposedFile.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ModelsExposedFile.


        :param file_size: The file_size of this ModelsExposedFile.
        :type file_size: int
        """

        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this ModelsExposedFile.


        :return: The file_type of this ModelsExposedFile.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ModelsExposedFile.


        :param file_type: The file_type of this ModelsExposedFile.
        :type file_type: str
        """

        self._file_type = file_type

    @property
    def file_url(self):
        """Gets the file_url of this ModelsExposedFile.


        :return: The file_url of this ModelsExposedFile.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this ModelsExposedFile.


        :param file_url: The file_url of this ModelsExposedFile.
        :type file_url: str
        """

        self._file_url = file_url

    @property
    def id(self):
        """Gets the id of this ModelsExposedFile.


        :return: The id of this ModelsExposedFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsExposedFile.


        :param id: The id of this ModelsExposedFile.
        :type id: int
        """

        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsExposedFile.


        :return: The updated_at of this ModelsExposedFile.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsExposedFile.


        :param updated_at: The updated_at of this ModelsExposedFile.
        :type updated_at: str
        """

        self._updated_at = updated_at
