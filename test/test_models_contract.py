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
from rainbowsdk.models.models_contract import ModelsContract  # noqa: E501
from rainbowsdk.rest import ApiException

class TestModelsContract(unittest.TestCase):
    """ModelsContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelsContract
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rainbowsdk.models.models_contract.ModelsContract()  # noqa: E501
        if include_optional :
            return ModelsContract(
                address = '', 
                app_id = 56, 
                auto_sponsor = True, 
                base_uri = '', 
                chain_id = 56, 
                chain_type = 56, 
                created_at = '', 
                deleted_at = rainbowsdk.models.gorm/deleted_at.gorm.DeletedAt(
                    time = '', 
                    valid = True, ), 
                error = '', 
                hash = '', 
                id = 56, 
                name = '', 
                owner_address = '', 
                royalties_address = '', 
                royalties_bps = 56, 
                status = 56, 
                symbol = '', 
                tokens_burnable = True, 
                tokens_transferable_by_admin = True, 
                tokens_transferable_by_user = True, 
                transfer_cooldown_time = 56, 
                tx_id = 56, 
                type = 56, 
                updated_at = ''
            )
        else :
            return ModelsContract(
        )

    def testModelsContract(self):
        """Test ModelsContract"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
