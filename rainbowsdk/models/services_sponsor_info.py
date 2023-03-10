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


class ServicesSponsorInfo(object):
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
        'collateral_sponsor': 'str',
        'collateral_sponsor_balance': 'str',
        'gas_sponsor': 'str',
        'gas_sponsor_balance': 'str',
        'gas_upper_bound': 'str',
        'is_all_white_listed': 'bool'
    }

    attribute_map = {
        'collateral_sponsor': 'collateral_sponsor',
        'collateral_sponsor_balance': 'collateral_sponsor_balance',
        'gas_sponsor': 'gas_sponsor',
        'gas_sponsor_balance': 'gas_sponsor_balance',
        'gas_upper_bound': 'gas_upper_bound',
        'is_all_white_listed': 'is_all_white_listed'
    }

    def __init__(self, collateral_sponsor=None, collateral_sponsor_balance=None, gas_sponsor=None, gas_sponsor_balance=None, gas_upper_bound=None, is_all_white_listed=None, local_vars_configuration=None):  # noqa: E501
        """ServicesSponsorInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._collateral_sponsor = None
        self._collateral_sponsor_balance = None
        self._gas_sponsor = None
        self._gas_sponsor_balance = None
        self._gas_upper_bound = None
        self._is_all_white_listed = None
        self.discriminator = None

        if collateral_sponsor is not None:
            self.collateral_sponsor = collateral_sponsor
        if collateral_sponsor_balance is not None:
            self.collateral_sponsor_balance = collateral_sponsor_balance
        if gas_sponsor is not None:
            self.gas_sponsor = gas_sponsor
        if gas_sponsor_balance is not None:
            self.gas_sponsor_balance = gas_sponsor_balance
        if gas_upper_bound is not None:
            self.gas_upper_bound = gas_upper_bound
        if is_all_white_listed is not None:
            self.is_all_white_listed = is_all_white_listed

    @property
    def collateral_sponsor(self):
        """Gets the collateral_sponsor of this ServicesSponsorInfo.  # noqa: E501


        :return: The collateral_sponsor of this ServicesSponsorInfo.  # noqa: E501
        :rtype: str
        """
        return self._collateral_sponsor

    @collateral_sponsor.setter
    def collateral_sponsor(self, collateral_sponsor):
        """Sets the collateral_sponsor of this ServicesSponsorInfo.


        :param collateral_sponsor: The collateral_sponsor of this ServicesSponsorInfo.  # noqa: E501
        :type collateral_sponsor: str
        """

        self._collateral_sponsor = collateral_sponsor

    @property
    def collateral_sponsor_balance(self):
        """Gets the collateral_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501


        :return: The collateral_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501
        :rtype: str
        """
        return self._collateral_sponsor_balance

    @collateral_sponsor_balance.setter
    def collateral_sponsor_balance(self, collateral_sponsor_balance):
        """Sets the collateral_sponsor_balance of this ServicesSponsorInfo.


        :param collateral_sponsor_balance: The collateral_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501
        :type collateral_sponsor_balance: str
        """

        self._collateral_sponsor_balance = collateral_sponsor_balance

    @property
    def gas_sponsor(self):
        """Gets the gas_sponsor of this ServicesSponsorInfo.  # noqa: E501


        :return: The gas_sponsor of this ServicesSponsorInfo.  # noqa: E501
        :rtype: str
        """
        return self._gas_sponsor

    @gas_sponsor.setter
    def gas_sponsor(self, gas_sponsor):
        """Sets the gas_sponsor of this ServicesSponsorInfo.


        :param gas_sponsor: The gas_sponsor of this ServicesSponsorInfo.  # noqa: E501
        :type gas_sponsor: str
        """

        self._gas_sponsor = gas_sponsor

    @property
    def gas_sponsor_balance(self):
        """Gets the gas_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501


        :return: The gas_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501
        :rtype: str
        """
        return self._gas_sponsor_balance

    @gas_sponsor_balance.setter
    def gas_sponsor_balance(self, gas_sponsor_balance):
        """Sets the gas_sponsor_balance of this ServicesSponsorInfo.


        :param gas_sponsor_balance: The gas_sponsor_balance of this ServicesSponsorInfo.  # noqa: E501
        :type gas_sponsor_balance: str
        """

        self._gas_sponsor_balance = gas_sponsor_balance

    @property
    def gas_upper_bound(self):
        """Gets the gas_upper_bound of this ServicesSponsorInfo.  # noqa: E501


        :return: The gas_upper_bound of this ServicesSponsorInfo.  # noqa: E501
        :rtype: str
        """
        return self._gas_upper_bound

    @gas_upper_bound.setter
    def gas_upper_bound(self, gas_upper_bound):
        """Sets the gas_upper_bound of this ServicesSponsorInfo.


        :param gas_upper_bound: The gas_upper_bound of this ServicesSponsorInfo.  # noqa: E501
        :type gas_upper_bound: str
        """

        self._gas_upper_bound = gas_upper_bound

    @property
    def is_all_white_listed(self):
        """Gets the is_all_white_listed of this ServicesSponsorInfo.  # noqa: E501


        :return: The is_all_white_listed of this ServicesSponsorInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_all_white_listed

    @is_all_white_listed.setter
    def is_all_white_listed(self, is_all_white_listed):
        """Sets the is_all_white_listed of this ServicesSponsorInfo.


        :param is_all_white_listed: The is_all_white_listed of this ServicesSponsorInfo.  # noqa: E501
        :type is_all_white_listed: bool
        """

        self._is_all_white_listed = is_all_white_listed

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
        if not isinstance(other, ServicesSponsorInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServicesSponsorInfo):
            return True

        return self.to_dict() != other.to_dict()
