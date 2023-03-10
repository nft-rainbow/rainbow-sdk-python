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
from rainbowsdk.api.files_api import FilesApi  # noqa: E501
from rainbowsdk.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = rainbowsdk.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_files(self):
        """Test case for list_files

        Obtain file list  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        Upload file  # noqa: E501
        """
        pass

    def test_upload_file_to_oss(self):
        """Test case for upload_file_to_oss

        Upload file to OSS  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
