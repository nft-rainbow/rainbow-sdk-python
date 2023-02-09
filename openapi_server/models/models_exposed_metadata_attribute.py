# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ModelsExposedMetadataAttribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attribute_name: str=None, display_type: str=None, trait_type: str=None, value: str=None):
        """ModelsExposedMetadataAttribute - a model defined in OpenAPI

        :param attribute_name: The attribute_name of this ModelsExposedMetadataAttribute.
        :param display_type: The display_type of this ModelsExposedMetadataAttribute.
        :param trait_type: The trait_type of this ModelsExposedMetadataAttribute.
        :param value: The value of this ModelsExposedMetadataAttribute.
        """
        self.openapi_types = {
            'attribute_name': str,
            'display_type': str,
            'trait_type': str,
            'value': str
        }

        self.attribute_map = {
            'attribute_name': 'attribute_name',
            'display_type': 'display_type',
            'trait_type': 'trait_type',
            'value': 'value'
        }

        self._attribute_name = attribute_name
        self._display_type = display_type
        self._trait_type = trait_type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelsExposedMetadataAttribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The models.ExposedMetadataAttribute of this ModelsExposedMetadataAttribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attribute_name(self):
        """Gets the attribute_name of this ModelsExposedMetadataAttribute.


        :return: The attribute_name of this ModelsExposedMetadataAttribute.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this ModelsExposedMetadataAttribute.


        :param attribute_name: The attribute_name of this ModelsExposedMetadataAttribute.
        :type attribute_name: str
        """

        self._attribute_name = attribute_name

    @property
    def display_type(self):
        """Gets the display_type of this ModelsExposedMetadataAttribute.


        :return: The display_type of this ModelsExposedMetadataAttribute.
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this ModelsExposedMetadataAttribute.


        :param display_type: The display_type of this ModelsExposedMetadataAttribute.
        :type display_type: str
        """

        self._display_type = display_type

    @property
    def trait_type(self):
        """Gets the trait_type of this ModelsExposedMetadataAttribute.


        :return: The trait_type of this ModelsExposedMetadataAttribute.
        :rtype: str
        """
        return self._trait_type

    @trait_type.setter
    def trait_type(self, trait_type):
        """Sets the trait_type of this ModelsExposedMetadataAttribute.


        :param trait_type: The trait_type of this ModelsExposedMetadataAttribute.
        :type trait_type: str
        """

        self._trait_type = trait_type

    @property
    def value(self):
        """Gets the value of this ModelsExposedMetadataAttribute.

        TODO support number

        :return: The value of this ModelsExposedMetadataAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelsExposedMetadataAttribute.

        TODO support number

        :param value: The value of this ModelsExposedMetadataAttribute.
        :type value: str
        """

        self._value = value