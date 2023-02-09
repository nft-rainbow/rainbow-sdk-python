# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ServicesContractAdminUpdateDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, admin_address: str=None):
        """ServicesContractAdminUpdateDto - a model defined in OpenAPI

        :param admin_address: The admin_address of this ServicesContractAdminUpdateDto.
        """
        self.openapi_types = {
            'admin_address': str
        }

        self.attribute_map = {
            'admin_address': 'admin_address'
        }

        self._admin_address = admin_address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServicesContractAdminUpdateDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The services.ContractAdminUpdateDto of this ServicesContractAdminUpdateDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def admin_address(self):
        """Gets the admin_address of this ServicesContractAdminUpdateDto.

        Chain           string `form:\"chain\" json:\"chain\" binding:\"required,oneof=conflux conflux_test\"` ContractAddress string `form:\"contract_address\" json:\"contract_address\" binding:\"required\"`

        :return: The admin_address of this ServicesContractAdminUpdateDto.
        :rtype: str
        """
        return self._admin_address

    @admin_address.setter
    def admin_address(self, admin_address):
        """Sets the admin_address of this ServicesContractAdminUpdateDto.

        Chain           string `form:\"chain\" json:\"chain\" binding:\"required,oneof=conflux conflux_test\"` ContractAddress string `form:\"contract_address\" json:\"contract_address\" binding:\"required\"`

        :param admin_address: The admin_address of this ServicesContractAdminUpdateDto.
        :type admin_address: str
        """
        if admin_address is None:
            raise ValueError("Invalid value for `admin_address`, must not be `None`")

        self._admin_address = admin_address