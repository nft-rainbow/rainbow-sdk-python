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
from rainbowsdk.api.mints_api import MintsApi  # noqa: E501
from rainbowsdk.rest import ApiException


class TestMintsApi(unittest.TestCase):
    """MintsApi unit test stubs"""

    def setUp(self):
        self.api = rainbowsdk.api.mints_api.MintsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_custom_mint(self):
        """Test case for batch_custom_mint

        Batch Mint NFTs  # noqa: E501
        """
        pass

    def test_custom_mint(self):
        """Test case for custom_mint

        Mint NFT  # noqa: E501
        """
        pass

    def test_easy_mint_by_file(self):
        """Test case for easy_mint_by_file

        Mint NFT with file  # noqa: E501
        """
        pass

    def test_easy_mint_by_metadata(self):
        """Test case for easy_mint_by_metadata

        Mint NFT with metadata  # noqa: E501
        """
        pass

    def test_get_mint_detail(self):
        """Test case for get_mint_detail

        Mint NFT detail  # noqa: E501
        """
        pass

    def test_list_mints(self):
        """Test case for list_mints

        Obtain NFT list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()