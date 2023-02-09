# coding: utf-8

"""
    Rainbow-API

    The responses of the open api in swagger focus on the data field rather than the code and the message fields  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from rainbowsdk.configuration import Configuration


class ServicesTransferBatchDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'chain': 'str',
        'contract_address': 'str',
        'contract_type': 'str',
        'items': 'list[ServicesTransferItemDto]'
    }

    attribute_map = {
        'chain': 'chain',
        'contract_address': 'contract_address',
        'contract_type': 'contract_type',
        'items': 'items'
    }

    def __init__(self, chain=None, contract_address=None, contract_type=None, items=None, local_vars_configuration=None):  # noqa: E501
        """ServicesTransferBatchDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._chain = None
        self._contract_address = None
        self._contract_type = None
        self._items = None
        self.discriminator = None

        self.chain = chain
        self.contract_address = contract_address
        self.contract_type = contract_type
        self.items = items

    @property
    def chain(self):
        """Gets the chain of this ServicesTransferBatchDto.  # noqa: E501


        :return: The chain of this ServicesTransferBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this ServicesTransferBatchDto.


        :param chain: The chain of this ServicesTransferBatchDto.  # noqa: E501
        :type chain: str
        """
        if self.local_vars_configuration.client_side_validation and chain is None:  # noqa: E501
            raise ValueError("Invalid value for `chain`, must not be `None`")  # noqa: E501
        allowed_values = ["conflux", "conflux_test"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and chain not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `chain` ({0}), must be one of {1}"  # noqa: E501
                .format(chain, allowed_values)
            )

        self._chain = chain

    @property
    def contract_address(self):
        """Gets the contract_address of this ServicesTransferBatchDto.  # noqa: E501


        :return: The contract_address of this ServicesTransferBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this ServicesTransferBatchDto.


        :param contract_address: The contract_address of this ServicesTransferBatchDto.  # noqa: E501
        :type contract_address: str
        """
        if self.local_vars_configuration.client_side_validation and contract_address is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

    @property
    def contract_type(self):
        """Gets the contract_type of this ServicesTransferBatchDto.  # noqa: E501


        :return: The contract_type of this ServicesTransferBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this ServicesTransferBatchDto.


        :param contract_type: The contract_type of this ServicesTransferBatchDto.  # noqa: E501
        :type contract_type: str
        """
        if self.local_vars_configuration.client_side_validation and contract_type is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_type`, must not be `None`")  # noqa: E501
        allowed_values = ["erc721", "erc1155"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and contract_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `contract_type` ({0}), must be one of {1}"  # noqa: E501
                .format(contract_type, allowed_values)
            )

        self._contract_type = contract_type

    @property
    def items(self):
        """Gets the items of this ServicesTransferBatchDto.  # noqa: E501


        :return: The items of this ServicesTransferBatchDto.  # noqa: E501
        :rtype: list[ServicesTransferItemDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ServicesTransferBatchDto.


        :param items: The items of this ServicesTransferBatchDto.  # noqa: E501
        :type items: list[ServicesTransferItemDto]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServicesTransferBatchDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServicesTransferBatchDto):
            return True

        return self.to_dict() != other.to_dict()
