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


class ModelsTransaction(object):
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
        'chain_id': 'int',
        'chain_type': 'int',
        'created_at': 'str',
        'data': 'str',
        'deleted_at': 'GormDeletedAt',
        'epoch_height': 'float',
        'epoch_number': 'int',
        'error': 'str',
        '_from': 'str',
        'gas': 'float',
        'gas_price': 'float',
        'hash': 'str',
        'id': 'int',
        'nonce': 'int',
        'pending_reason': 'str',
        'state': 'int',
        'storage_limit': 'float',
        'task_type': 'int',
        'to': 'str',
        'updated_at': 'str',
        'value': 'float'
    }

    attribute_map = {
        'chain_id': 'chainId',
        'chain_type': 'chainType',
        'created_at': 'created_at',
        'data': 'data',
        'deleted_at': 'deleted_at',
        'epoch_height': 'epochHeight',
        'epoch_number': 'epoch_number',
        'error': 'error',
        '_from': 'from',
        'gas': 'gas',
        'gas_price': 'gasPrice',
        'hash': 'hash',
        'id': 'id',
        'nonce': 'nonce',
        'pending_reason': 'pending_reason',
        'state': 'state',
        'storage_limit': 'storageLimit',
        'task_type': 'taskType',
        'to': 'to',
        'updated_at': 'updated_at',
        'value': 'value'
    }

    def __init__(self, chain_id=None, chain_type=None, created_at=None, data=None, deleted_at=None, epoch_height=None, epoch_number=None, error=None, _from=None, gas=None, gas_price=None, hash=None, id=None, nonce=None, pending_reason=None, state=None, storage_limit=None, task_type=None, to=None, updated_at=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ModelsTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._chain_id = None
        self._chain_type = None
        self._created_at = None
        self._data = None
        self._deleted_at = None
        self._epoch_height = None
        self._epoch_number = None
        self._error = None
        self.__from = None
        self._gas = None
        self._gas_price = None
        self._hash = None
        self._id = None
        self._nonce = None
        self._pending_reason = None
        self._state = None
        self._storage_limit = None
        self._task_type = None
        self._to = None
        self._updated_at = None
        self._value = None
        self.discriminator = None

        if chain_id is not None:
            self.chain_id = chain_id
        if chain_type is not None:
            self.chain_type = chain_type
        if created_at is not None:
            self.created_at = created_at
        if data is not None:
            self.data = data
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if epoch_height is not None:
            self.epoch_height = epoch_height
        if epoch_number is not None:
            self.epoch_number = epoch_number
        if error is not None:
            self.error = error
        if _from is not None:
            self._from = _from
        if gas is not None:
            self.gas = gas
        if gas_price is not None:
            self.gas_price = gas_price
        if hash is not None:
            self.hash = hash
        if id is not None:
            self.id = id
        if nonce is not None:
            self.nonce = nonce
        if pending_reason is not None:
            self.pending_reason = pending_reason
        if state is not None:
            self.state = state
        if storage_limit is not None:
            self.storage_limit = storage_limit
        if task_type is not None:
            self.task_type = task_type
        if to is not None:
            self.to = to
        if updated_at is not None:
            self.updated_at = updated_at
        if value is not None:
            self.value = value

    @property
    def chain_id(self):
        """Gets the chain_id of this ModelsTransaction.  # noqa: E501


        :return: The chain_id of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ModelsTransaction.


        :param chain_id: The chain_id of this ModelsTransaction.  # noqa: E501
        :type chain_id: int
        """

        self._chain_id = chain_id

    @property
    def chain_type(self):
        """Gets the chain_type of this ModelsTransaction.  # noqa: E501


        :return: The chain_type of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._chain_type

    @chain_type.setter
    def chain_type(self, chain_type):
        """Sets the chain_type of this ModelsTransaction.


        :param chain_type: The chain_type of this ModelsTransaction.  # noqa: E501
        :type chain_type: int
        """

        self._chain_type = chain_type

    @property
    def created_at(self):
        """Gets the created_at of this ModelsTransaction.  # noqa: E501


        :return: The created_at of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsTransaction.


        :param created_at: The created_at of this ModelsTransaction.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def data(self):
        """Gets the data of this ModelsTransaction.  # noqa: E501


        :return: The data of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ModelsTransaction.


        :param data: The data of this ModelsTransaction.  # noqa: E501
        :type data: str
        """

        self._data = data

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsTransaction.  # noqa: E501


        :return: The deleted_at of this ModelsTransaction.  # noqa: E501
        :rtype: GormDeletedAt
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsTransaction.


        :param deleted_at: The deleted_at of this ModelsTransaction.  # noqa: E501
        :type deleted_at: GormDeletedAt
        """

        self._deleted_at = deleted_at

    @property
    def epoch_height(self):
        """Gets the epoch_height of this ModelsTransaction.  # noqa: E501


        :return: The epoch_height of this ModelsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._epoch_height

    @epoch_height.setter
    def epoch_height(self, epoch_height):
        """Sets the epoch_height of this ModelsTransaction.


        :param epoch_height: The epoch_height of this ModelsTransaction.  # noqa: E501
        :type epoch_height: float
        """

        self._epoch_height = epoch_height

    @property
    def epoch_number(self):
        """Gets the epoch_number of this ModelsTransaction.  # noqa: E501


        :return: The epoch_number of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._epoch_number

    @epoch_number.setter
    def epoch_number(self, epoch_number):
        """Sets the epoch_number of this ModelsTransaction.


        :param epoch_number: The epoch_number of this ModelsTransaction.  # noqa: E501
        :type epoch_number: int
        """

        self._epoch_number = epoch_number

    @property
    def error(self):
        """Gets the error of this ModelsTransaction.  # noqa: E501


        :return: The error of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ModelsTransaction.


        :param error: The error of this ModelsTransaction.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def _from(self):
        """Gets the _from of this ModelsTransaction.  # noqa: E501


        :return: The _from of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ModelsTransaction.


        :param _from: The _from of this ModelsTransaction.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

    @property
    def gas(self):
        """Gets the gas of this ModelsTransaction.  # noqa: E501


        :return: The gas of this ModelsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._gas

    @gas.setter
    def gas(self, gas):
        """Sets the gas of this ModelsTransaction.


        :param gas: The gas of this ModelsTransaction.  # noqa: E501
        :type gas: float
        """

        self._gas = gas

    @property
    def gas_price(self):
        """Gets the gas_price of this ModelsTransaction.  # noqa: E501


        :return: The gas_price of this ModelsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._gas_price

    @gas_price.setter
    def gas_price(self, gas_price):
        """Sets the gas_price of this ModelsTransaction.


        :param gas_price: The gas_price of this ModelsTransaction.  # noqa: E501
        :type gas_price: float
        """

        self._gas_price = gas_price

    @property
    def hash(self):
        """Gets the hash of this ModelsTransaction.  # noqa: E501


        :return: The hash of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ModelsTransaction.


        :param hash: The hash of this ModelsTransaction.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this ModelsTransaction.  # noqa: E501


        :return: The id of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsTransaction.


        :param id: The id of this ModelsTransaction.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def nonce(self):
        """Gets the nonce of this ModelsTransaction.  # noqa: E501


        :return: The nonce of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this ModelsTransaction.


        :param nonce: The nonce of this ModelsTransaction.  # noqa: E501
        :type nonce: int
        """

        self._nonce = nonce

    @property
    def pending_reason(self):
        """Gets the pending_reason of this ModelsTransaction.  # noqa: E501


        :return: The pending_reason of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._pending_reason

    @pending_reason.setter
    def pending_reason(self, pending_reason):
        """Sets the pending_reason of this ModelsTransaction.


        :param pending_reason: The pending_reason of this ModelsTransaction.  # noqa: E501
        :type pending_reason: str
        """

        self._pending_reason = pending_reason

    @property
    def state(self):
        """Gets the state of this ModelsTransaction.  # noqa: E501


        :return: The state of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ModelsTransaction.


        :param state: The state of this ModelsTransaction.  # noqa: E501
        :type state: int
        """

        self._state = state

    @property
    def storage_limit(self):
        """Gets the storage_limit of this ModelsTransaction.  # noqa: E501


        :return: The storage_limit of this ModelsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._storage_limit

    @storage_limit.setter
    def storage_limit(self, storage_limit):
        """Sets the storage_limit of this ModelsTransaction.


        :param storage_limit: The storage_limit of this ModelsTransaction.  # noqa: E501
        :type storage_limit: float
        """

        self._storage_limit = storage_limit

    @property
    def task_type(self):
        """Gets the task_type of this ModelsTransaction.  # noqa: E501


        :return: The task_type of this ModelsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ModelsTransaction.


        :param task_type: The task_type of this ModelsTransaction.  # noqa: E501
        :type task_type: int
        """

        self._task_type = task_type

    @property
    def to(self):
        """Gets the to of this ModelsTransaction.  # noqa: E501


        :return: The to of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ModelsTransaction.


        :param to: The to of this ModelsTransaction.  # noqa: E501
        :type to: str
        """

        self._to = to

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsTransaction.  # noqa: E501


        :return: The updated_at of this ModelsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsTransaction.


        :param updated_at: The updated_at of this ModelsTransaction.  # noqa: E501
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this ModelsTransaction.  # noqa: E501


        :return: The value of this ModelsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelsTransaction.


        :param value: The value of this ModelsTransaction.  # noqa: E501
        :type value: float
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
        if not isinstance(other, ModelsTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTransaction):
            return True

        return self.to_dict() != other.to_dict()
