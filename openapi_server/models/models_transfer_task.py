# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.gorm_deleted_at import GormDeletedAt
from openapi_server import util


class ModelsTransferTask(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: int=None, app_id: int=None, chain_id: int=None, chain_type: int=None, contract: str=None, contract_type: int=None, created_at: str=None, deleted_at: GormDeletedAt=None, error: str=None, hash: str=None, id: int=None, status: int=None, token_id: str=None, transfer_from: str=None, transfer_to: str=None, tx_id: int=None, updated_at: str=None):
        """ModelsTransferTask - a model defined in OpenAPI

        :param amount: The amount of this ModelsTransferTask.
        :param app_id: The app_id of this ModelsTransferTask.
        :param chain_id: The chain_id of this ModelsTransferTask.
        :param chain_type: The chain_type of this ModelsTransferTask.
        :param contract: The contract of this ModelsTransferTask.
        :param contract_type: The contract_type of this ModelsTransferTask.
        :param created_at: The created_at of this ModelsTransferTask.
        :param deleted_at: The deleted_at of this ModelsTransferTask.
        :param error: The error of this ModelsTransferTask.
        :param hash: The hash of this ModelsTransferTask.
        :param id: The id of this ModelsTransferTask.
        :param status: The status of this ModelsTransferTask.
        :param token_id: The token_id of this ModelsTransferTask.
        :param transfer_from: The transfer_from of this ModelsTransferTask.
        :param transfer_to: The transfer_to of this ModelsTransferTask.
        :param tx_id: The tx_id of this ModelsTransferTask.
        :param updated_at: The updated_at of this ModelsTransferTask.
        """
        self.openapi_types = {
            'amount': int,
            'app_id': int,
            'chain_id': int,
            'chain_type': int,
            'contract': str,
            'contract_type': int,
            'created_at': str,
            'deleted_at': GormDeletedAt,
            'error': str,
            'hash': str,
            'id': int,
            'status': int,
            'token_id': str,
            'transfer_from': str,
            'transfer_to': str,
            'tx_id': int,
            'updated_at': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'app_id': 'app_id',
            'chain_id': 'chain_id',
            'chain_type': 'chain_type',
            'contract': 'contract',
            'contract_type': 'contract_type',
            'created_at': 'created_at',
            'deleted_at': 'deleted_at',
            'error': 'error',
            'hash': 'hash',
            'id': 'id',
            'status': 'status',
            'token_id': 'token_id',
            'transfer_from': 'transfer_from',
            'transfer_to': 'transfer_to',
            'tx_id': 'tx_id',
            'updated_at': 'updated_at'
        }

        self._amount = amount
        self._app_id = app_id
        self._chain_id = chain_id
        self._chain_type = chain_type
        self._contract = contract
        self._contract_type = contract_type
        self._created_at = created_at
        self._deleted_at = deleted_at
        self._error = error
        self._hash = hash
        self._id = id
        self._status = status
        self._token_id = token_id
        self._transfer_from = transfer_from
        self._transfer_to = transfer_to
        self._tx_id = tx_id
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelsTransferTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The models.TransferTask of this ModelsTransferTask.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this ModelsTransferTask.


        :return: The amount of this ModelsTransferTask.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ModelsTransferTask.


        :param amount: The amount of this ModelsTransferTask.
        :type amount: int
        """

        self._amount = amount

    @property
    def app_id(self):
        """Gets the app_id of this ModelsTransferTask.


        :return: The app_id of this ModelsTransferTask.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ModelsTransferTask.


        :param app_id: The app_id of this ModelsTransferTask.
        :type app_id: int
        """

        self._app_id = app_id

    @property
    def chain_id(self):
        """Gets the chain_id of this ModelsTransferTask.


        :return: The chain_id of this ModelsTransferTask.
        :rtype: int
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ModelsTransferTask.


        :param chain_id: The chain_id of this ModelsTransferTask.
        :type chain_id: int
        """

        self._chain_id = chain_id

    @property
    def chain_type(self):
        """Gets the chain_type of this ModelsTransferTask.


        :return: The chain_type of this ModelsTransferTask.
        :rtype: int
        """
        return self._chain_type

    @chain_type.setter
    def chain_type(self, chain_type):
        """Sets the chain_type of this ModelsTransferTask.


        :param chain_type: The chain_type of this ModelsTransferTask.
        :type chain_type: int
        """

        self._chain_type = chain_type

    @property
    def contract(self):
        """Gets the contract of this ModelsTransferTask.


        :return: The contract of this ModelsTransferTask.
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this ModelsTransferTask.


        :param contract: The contract of this ModelsTransferTask.
        :type contract: str
        """

        self._contract = contract

    @property
    def contract_type(self):
        """Gets the contract_type of this ModelsTransferTask.


        :return: The contract_type of this ModelsTransferTask.
        :rtype: int
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this ModelsTransferTask.


        :param contract_type: The contract_type of this ModelsTransferTask.
        :type contract_type: int
        """

        self._contract_type = contract_type

    @property
    def created_at(self):
        """Gets the created_at of this ModelsTransferTask.


        :return: The created_at of this ModelsTransferTask.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsTransferTask.


        :param created_at: The created_at of this ModelsTransferTask.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsTransferTask.


        :return: The deleted_at of this ModelsTransferTask.
        :rtype: GormDeletedAt
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsTransferTask.


        :param deleted_at: The deleted_at of this ModelsTransferTask.
        :type deleted_at: GormDeletedAt
        """

        self._deleted_at = deleted_at

    @property
    def error(self):
        """Gets the error of this ModelsTransferTask.


        :return: The error of this ModelsTransferTask.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ModelsTransferTask.


        :param error: The error of this ModelsTransferTask.
        :type error: str
        """

        self._error = error

    @property
    def hash(self):
        """Gets the hash of this ModelsTransferTask.


        :return: The hash of this ModelsTransferTask.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ModelsTransferTask.


        :param hash: The hash of this ModelsTransferTask.
        :type hash: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this ModelsTransferTask.


        :return: The id of this ModelsTransferTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsTransferTask.


        :param id: The id of this ModelsTransferTask.
        :type id: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this ModelsTransferTask.

        0-pending, 1-success, 2-failed

        :return: The status of this ModelsTransferTask.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelsTransferTask.

        0-pending, 1-success, 2-failed

        :param status: The status of this ModelsTransferTask.
        :type status: int
        """

        self._status = status

    @property
    def token_id(self):
        """Gets the token_id of this ModelsTransferTask.


        :return: The token_id of this ModelsTransferTask.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this ModelsTransferTask.


        :param token_id: The token_id of this ModelsTransferTask.
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def transfer_from(self):
        """Gets the transfer_from of this ModelsTransferTask.


        :return: The transfer_from of this ModelsTransferTask.
        :rtype: str
        """
        return self._transfer_from

    @transfer_from.setter
    def transfer_from(self, transfer_from):
        """Sets the transfer_from of this ModelsTransferTask.


        :param transfer_from: The transfer_from of this ModelsTransferTask.
        :type transfer_from: str
        """

        self._transfer_from = transfer_from

    @property
    def transfer_to(self):
        """Gets the transfer_to of this ModelsTransferTask.


        :return: The transfer_to of this ModelsTransferTask.
        :rtype: str
        """
        return self._transfer_to

    @transfer_to.setter
    def transfer_to(self, transfer_to):
        """Sets the transfer_to of this ModelsTransferTask.


        :param transfer_to: The transfer_to of this ModelsTransferTask.
        :type transfer_to: str
        """

        self._transfer_to = transfer_to

    @property
    def tx_id(self):
        """Gets the tx_id of this ModelsTransferTask.


        :return: The tx_id of this ModelsTransferTask.
        :rtype: int
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this ModelsTransferTask.


        :param tx_id: The tx_id of this ModelsTransferTask.
        :type tx_id: int
        """

        self._tx_id = tx_id

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsTransferTask.


        :return: The updated_at of this ModelsTransferTask.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsTransferTask.


        :param updated_at: The updated_at of this ModelsTransferTask.
        :type updated_at: str
        """

        self._updated_at = updated_at
