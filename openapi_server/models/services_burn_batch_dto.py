# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.services_burn_item_dto import ServicesBurnItemDto
from openapi_server import util


class ServicesBurnBatchDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, chain: str=None, contract_address: str=None, contract_type: str=None, items: List[ServicesBurnItemDto]=None, user: str=None):
        """ServicesBurnBatchDto - a model defined in OpenAPI

        :param chain: The chain of this ServicesBurnBatchDto.
        :param contract_address: The contract_address of this ServicesBurnBatchDto.
        :param contract_type: The contract_type of this ServicesBurnBatchDto.
        :param items: The items of this ServicesBurnBatchDto.
        :param user: The user of this ServicesBurnBatchDto.
        """
        self.openapi_types = {
            'chain': str,
            'contract_address': str,
            'contract_type': str,
            'items': List[ServicesBurnItemDto],
            'user': str
        }

        self.attribute_map = {
            'chain': 'chain',
            'contract_address': 'contract_address',
            'contract_type': 'contract_type',
            'items': 'items',
            'user': 'user'
        }

        self._chain = chain
        self._contract_address = contract_address
        self._contract_type = contract_type
        self._items = items
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServicesBurnBatchDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The services.BurnBatchDto of this ServicesBurnBatchDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chain(self):
        """Gets the chain of this ServicesBurnBatchDto.


        :return: The chain of this ServicesBurnBatchDto.
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this ServicesBurnBatchDto.


        :param chain: The chain of this ServicesBurnBatchDto.
        :type chain: str
        """
        allowed_values = ["conflux", "conflux_test"]  # noqa: E501
        if chain not in allowed_values:
            raise ValueError(
                "Invalid value for `chain` ({0}), must be one of {1}"
                .format(chain, allowed_values)
            )

        self._chain = chain

    @property
    def contract_address(self):
        """Gets the contract_address of this ServicesBurnBatchDto.


        :return: The contract_address of this ServicesBurnBatchDto.
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this ServicesBurnBatchDto.


        :param contract_address: The contract_address of this ServicesBurnBatchDto.
        :type contract_address: str
        """
        if contract_address is None:
            raise ValueError("Invalid value for `contract_address`, must not be `None`")

        self._contract_address = contract_address

    @property
    def contract_type(self):
        """Gets the contract_type of this ServicesBurnBatchDto.


        :return: The contract_type of this ServicesBurnBatchDto.
        :rtype: str
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this ServicesBurnBatchDto.


        :param contract_type: The contract_type of this ServicesBurnBatchDto.
        :type contract_type: str
        """
        allowed_values = ["erc721", "erc1155"]  # noqa: E501
        if contract_type not in allowed_values:
            raise ValueError(
                "Invalid value for `contract_type` ({0}), must be one of {1}"
                .format(contract_type, allowed_values)
            )

        self._contract_type = contract_type

    @property
    def items(self):
        """Gets the items of this ServicesBurnBatchDto.


        :return: The items of this ServicesBurnBatchDto.
        :rtype: List[ServicesBurnItemDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ServicesBurnBatchDto.


        :param items: The items of this ServicesBurnBatchDto.
        :type items: List[ServicesBurnItemDto]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def user(self):
        """Gets the user of this ServicesBurnBatchDto.


        :return: The user of this ServicesBurnBatchDto.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ServicesBurnBatchDto.


        :param user: The user of this ServicesBurnBatchDto.
        :type user: str
        """

        self._user = user
