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


class ModelsExposedMetadataAttribute(object):
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
        'attribute_name': 'str',
        'display_type': 'str',
        'trait_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attribute_name': 'attribute_name',
        'display_type': 'display_type',
        'trait_type': 'trait_type',
        'value': 'value'
    }

    def __init__(self, attribute_name=None, display_type=None, trait_type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ModelsExposedMetadataAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_name = None
        self._display_type = None
        self._trait_type = None
        self._value = None
        self.discriminator = None

        if attribute_name is not None:
            self.attribute_name = attribute_name
        if display_type is not None:
            self.display_type = display_type
        if trait_type is not None:
            self.trait_type = trait_type
        if value is not None:
            self.value = value

    @property
    def attribute_name(self):
        """Gets the attribute_name of this ModelsExposedMetadataAttribute.  # noqa: E501


        :return: The attribute_name of this ModelsExposedMetadataAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this ModelsExposedMetadataAttribute.


        :param attribute_name: The attribute_name of this ModelsExposedMetadataAttribute.  # noqa: E501
        :type attribute_name: str
        """

        self._attribute_name = attribute_name

    @property
    def display_type(self):
        """Gets the display_type of this ModelsExposedMetadataAttribute.  # noqa: E501


        :return: The display_type of this ModelsExposedMetadataAttribute.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this ModelsExposedMetadataAttribute.


        :param display_type: The display_type of this ModelsExposedMetadataAttribute.  # noqa: E501
        :type display_type: str
        """

        self._display_type = display_type

    @property
    def trait_type(self):
        """Gets the trait_type of this ModelsExposedMetadataAttribute.  # noqa: E501


        :return: The trait_type of this ModelsExposedMetadataAttribute.  # noqa: E501
        :rtype: str
        """
        return self._trait_type

    @trait_type.setter
    def trait_type(self, trait_type):
        """Sets the trait_type of this ModelsExposedMetadataAttribute.


        :param trait_type: The trait_type of this ModelsExposedMetadataAttribute.  # noqa: E501
        :type trait_type: str
        """

        self._trait_type = trait_type

    @property
    def value(self):
        """Gets the value of this ModelsExposedMetadataAttribute.  # noqa: E501

        TODO support number  # noqa: E501

        :return: The value of this ModelsExposedMetadataAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelsExposedMetadataAttribute.

        TODO support number  # noqa: E501

        :param value: The value of this ModelsExposedMetadataAttribute.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, ModelsExposedMetadataAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsExposedMetadataAttribute):
            return True

        return self.to_dict() != other.to_dict()