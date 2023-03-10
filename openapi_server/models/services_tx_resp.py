# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ServicesTxResp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error_msg: str=None, hash: str=None, is_finalized: bool=None, is_success: bool=None, state_code: int=None, state_msg: str=None):
        """ServicesTxResp - a model defined in OpenAPI

        :param error_msg: The error_msg of this ServicesTxResp.
        :param hash: The hash of this ServicesTxResp.
        :param is_finalized: The is_finalized of this ServicesTxResp.
        :param is_success: The is_success of this ServicesTxResp.
        :param state_code: The state_code of this ServicesTxResp.
        :param state_msg: The state_msg of this ServicesTxResp.
        """
        self.openapi_types = {
            'error_msg': str,
            'hash': str,
            'is_finalized': bool,
            'is_success': bool,
            'state_code': int,
            'state_msg': str
        }

        self.attribute_map = {
            'error_msg': 'error_msg',
            'hash': 'hash',
            'is_finalized': 'is_finalized',
            'is_success': 'is_success',
            'state_code': 'state_code',
            'state_msg': 'state_msg'
        }

        self._error_msg = error_msg
        self._hash = hash
        self._is_finalized = is_finalized
        self._is_success = is_success
        self._state_code = state_code
        self._state_msg = state_msg

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServicesTxResp':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The services.TxResp of this ServicesTxResp.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_msg(self):
        """Gets the error_msg of this ServicesTxResp.


        :return: The error_msg of this ServicesTxResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ServicesTxResp.


        :param error_msg: The error_msg of this ServicesTxResp.
        :type error_msg: str
        """

        self._error_msg = error_msg

    @property
    def hash(self):
        """Gets the hash of this ServicesTxResp.


        :return: The hash of this ServicesTxResp.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ServicesTxResp.


        :param hash: The hash of this ServicesTxResp.
        :type hash: str
        """

        self._hash = hash

    @property
    def is_finalized(self):
        """Gets the is_finalized of this ServicesTxResp.


        :return: The is_finalized of this ServicesTxResp.
        :rtype: bool
        """
        return self._is_finalized

    @is_finalized.setter
    def is_finalized(self, is_finalized):
        """Sets the is_finalized of this ServicesTxResp.


        :param is_finalized: The is_finalized of this ServicesTxResp.
        :type is_finalized: bool
        """

        self._is_finalized = is_finalized

    @property
    def is_success(self):
        """Gets the is_success of this ServicesTxResp.


        :return: The is_success of this ServicesTxResp.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ServicesTxResp.


        :param is_success: The is_success of this ServicesTxResp.
        :type is_success: bool
        """

        self._is_success = is_success

    @property
    def state_code(self):
        """Gets the state_code of this ServicesTxResp.


        :return: The state_code of this ServicesTxResp.
        :rtype: int
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this ServicesTxResp.


        :param state_code: The state_code of this ServicesTxResp.
        :type state_code: int
        """

        self._state_code = state_code

    @property
    def state_msg(self):
        """Gets the state_msg of this ServicesTxResp.


        :return: The state_msg of this ServicesTxResp.
        :rtype: str
        """
        return self._state_msg

    @state_msg.setter
    def state_msg(self, state_msg):
        """Sets the state_msg of this ServicesTxResp.


        :param state_msg: The state_msg of this ServicesTxResp.
        :type state_msg: str
        """

        self._state_msg = state_msg
