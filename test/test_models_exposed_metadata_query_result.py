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
from rainbowsdk.models.models_exposed_metadata_query_result import ModelsExposedMetadataQueryResult  # noqa: E501
from rainbowsdk.rest import ApiException

class TestModelsExposedMetadataQueryResult(unittest.TestCase):
    """ModelsExposedMetadataQueryResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelsExposedMetadataQueryResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rainbowsdk.models.models_exposed_metadata_query_result.ModelsExposedMetadataQueryResult()  # noqa: E501
        if include_optional :
            return ModelsExposedMetadataQueryResult(
                count = 56, 
                items = [
                    rainbowsdk.models.models/exposed_metadata.models.ExposedMetadata(
                        animation_url = '', 
                        attributes = [
                            rainbowsdk.models.models/exposed_metadata_attribute.models.ExposedMetadataAttribute(
                                attribute_name = '', 
                                display_type = '', 
                                trait_type = '', 
                                value = '', )
                            ], 
                        created_at = '', 
                        deleted_at = rainbowsdk.models.gorm/deleted_at.gorm.DeletedAt(
                            time = '', 
                            valid = True, ), 
                        description = '', 
                        external_link = '', 
                        id = 56, 
                        image = '', 
                        metadata_id = '', 
                        name = '', 
                        updated_at = '', 
                        uri = '', )
                    ]
            )
        else :
            return ModelsExposedMetadataQueryResult(
        )

    def testModelsExposedMetadataQueryResult(self):
        """Test ModelsExposedMetadataQueryResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
