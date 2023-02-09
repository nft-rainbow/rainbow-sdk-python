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
from rainbowsdk.api.transfers_api import TransfersApi  # noqa: E501
from rainbowsdk.rest import ApiException


class TestTransfersApi(unittest.TestCase):
    """TransfersApi unit test stubs"""

    def setUp(self):
        self.api = rainbowsdk.api.transfers_api.TransfersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_transfer_nft(self):
        """Test case for batch_transfer_nft

        Batch Transfer NFTs  # noqa: E501
        """
        pass

    def test_get_transfer_detail(self):
        """Test case for get_transfer_detail

        Transfer NFT detail  # noqa: E501
        """
        pass

    def test_list_transfer(self):
        """Test case for list_transfer

        Obtain the transferred NFTs list  # noqa: E501
        """
        pass

    def test_transfer_nft(self):
        """Test case for transfer_nft

        Transfer NFT  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()