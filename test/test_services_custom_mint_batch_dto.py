# coding: utf-8

"""
    Rainbow-API

    The responses of the open api in swagger focus on the data field rather than the code and the message fields  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rainbowsdk
from rainbowsdk.models.services_custom_mint_batch_dto import ServicesCustomMintBatchDto  # noqa: E501
from rainbowsdk.rest import ApiException

class TestServicesCustomMintBatchDto(unittest.TestCase):
    """ServicesCustomMintBatchDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServicesCustomMintBatchDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rainbowsdk.models.services_custom_mint_batch_dto.ServicesCustomMintBatchDto()  # noqa: E501
        if include_optional :
            return ServicesCustomMintBatchDto(
                chain = 'conflux', 
                contract_address = '', 
                mint_items = [
                    rainbowsdk.models.services/mint_item_dto.services.MintItemDto(
                        amount = 56, 
                        metadata_uri = '', 
                        mint_to_address = '', 
                        token_id = '', )
                    ]
            )
        else :
            return ServicesCustomMintBatchDto(
                chain = 'conflux',
                contract_address = '',
                mint_items = [
                    rainbowsdk.models.services/mint_item_dto.services.MintItemDto(
                        amount = 56, 
                        metadata_uri = '', 
                        mint_to_address = '', 
                        token_id = '', )
                    ],
        )

    def testServicesCustomMintBatchDto(self):
        """Test ServicesCustomMintBatchDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
