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
from rainbowsdk.api.login_api import LoginApi  # noqa: E501
from rainbowsdk.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = rainbowsdk.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_app(self):
        """Test case for login_app

        App login  # noqa: E501
        """
        pass

    def test_refresh_auth(self):
        """Test case for refresh_auth

        Refresh JWT  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
