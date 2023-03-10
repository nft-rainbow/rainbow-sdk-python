# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ServicesEasyMintMetaDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, chain: str=None, description: str=None, file_url: str=None, mint_to_address: str=None, name: str=None):
        """ServicesEasyMintMetaDto - a model defined in OpenAPI

        :param chain: The chain of this ServicesEasyMintMetaDto.
        :param description: The description of this ServicesEasyMintMetaDto.
        :param file_url: The file_url of this ServicesEasyMintMetaDto.
        :param mint_to_address: The mint_to_address of this ServicesEasyMintMetaDto.
        :param name: The name of this ServicesEasyMintMetaDto.
        """
        self.openapi_types = {
            'chain': str,
            'description': str,
            'file_url': str,
            'mint_to_address': str,
            'name': str
        }

        self.attribute_map = {
            'chain': 'chain',
            'description': 'description',
            'file_url': 'file_url',
            'mint_to_address': 'mint_to_address',
            'name': 'name'
        }

        self._chain = chain
        self._description = description
        self._file_url = file_url
        self._mint_to_address = mint_to_address
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServicesEasyMintMetaDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The services.EasyMintMetaDto of this ServicesEasyMintMetaDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chain(self):
        """Gets the chain of this ServicesEasyMintMetaDto.


        :return: The chain of this ServicesEasyMintMetaDto.
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this ServicesEasyMintMetaDto.


        :param chain: The chain of this ServicesEasyMintMetaDto.
        :type chain: str
        """
        if chain is None:
            raise ValueError("Invalid value for `chain`, must not be `None`")

        self._chain = chain

    @property
    def description(self):
        """Gets the description of this ServicesEasyMintMetaDto.


        :return: The description of this ServicesEasyMintMetaDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServicesEasyMintMetaDto.


        :param description: The description of this ServicesEasyMintMetaDto.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def file_url(self):
        """Gets the file_url of this ServicesEasyMintMetaDto.


        :return: The file_url of this ServicesEasyMintMetaDto.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this ServicesEasyMintMetaDto.


        :param file_url: The file_url of this ServicesEasyMintMetaDto.
        :type file_url: str
        """
        if file_url is None:
            raise ValueError("Invalid value for `file_url`, must not be `None`")

        self._file_url = file_url

    @property
    def mint_to_address(self):
        """Gets the mint_to_address of this ServicesEasyMintMetaDto.


        :return: The mint_to_address of this ServicesEasyMintMetaDto.
        :rtype: str
        """
        return self._mint_to_address

    @mint_to_address.setter
    def mint_to_address(self, mint_to_address):
        """Sets the mint_to_address of this ServicesEasyMintMetaDto.


        :param mint_to_address: The mint_to_address of this ServicesEasyMintMetaDto.
        :type mint_to_address: str
        """
        if mint_to_address is None:
            raise ValueError("Invalid value for `mint_to_address`, must not be `None`")

        self._mint_to_address = mint_to_address

    @property
    def name(self):
        """Gets the name of this ServicesEasyMintMetaDto.


        :return: The name of this ServicesEasyMintMetaDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServicesEasyMintMetaDto.


        :param name: The name of this ServicesEasyMintMetaDto.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
