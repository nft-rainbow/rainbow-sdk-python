# coding: utf-8

"""
    Rainbow-API

    The responses of the open api in swagger focus on the data field rather than the code and the message fields  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rainbowsdk
from rainbowsdk.api.transaction_api import TransactionApi  # noqa: E501
from rainbowsdk.rest import ApiException


class TestTransactionApi(unittest.TestCase):
    """TransactionApi unit test stubs"""

    def setUp(self):
        self.api = rainbowsdk.api.transaction_api.TransactionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transaction_by_id(self):
        """Test case for get_transaction_by_id

        Get transaction informantion by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
