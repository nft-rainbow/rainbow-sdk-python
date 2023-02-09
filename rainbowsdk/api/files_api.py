# coding: utf-8

"""
    Rainbow-API

    The responses of the open api in swagger focus on the data field rather than the code and the message fields  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rainbowsdk.api_client import ApiClient
from rainbowsdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_files(self, authorization, **kwargs):  # noqa: E501
        """Obtain file list  # noqa: E501

        Get the file list containing the info of the files uploaded in the specified app  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_files(authorization, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param page: page
        :type page: str
        :param limit: limit
        :type limit: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ModelsFilesQueryResult
        """
        kwargs['_return_http_data_only'] = True
        return self.list_files_with_http_info(authorization, **kwargs)  # noqa: E501

    def list_files_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Obtain file list  # noqa: E501

        Get the file list containing the info of the files uploaded in the specified app  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_files_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param page: page
        :type page: str
        :param limit: limit
        :type limit: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ModelsFilesQueryResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'authorization',
            'page',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_files" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and local_var_params.get('authorization') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization` when calling `list_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('page') is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "ModelsFilesQueryResult",
            500: "RainbowErrorsRainbowErrorDetailInfo",
        }

        return self.api_client.call_api(
            '/files/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def upload_file(self, authorization, file, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        Upload a file which can be a video, an image and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file(authorization, file, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param file: uploaded file (required)
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ServicesUploadFilesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_file_with_http_info(authorization, file, **kwargs)  # noqa: E501

    def upload_file_with_http_info(self, authorization, file, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        Upload a file which can be a video, an image and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file_with_http_info(authorization, file, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param file: uploaded file (required)
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ServicesUploadFilesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'authorization',
            'file'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and local_var_params.get('authorization') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and local_var_params.get('file') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `upload_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "ServicesUploadFilesResponse",
            500: "RainbowErrorsRainbowErrorDetailInfo",
        }

        return self.api_client.call_api(
            '/files/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def upload_file_to_oss(self, authorization, file, **kwargs):  # noqa: E501
        """Upload file to OSS  # noqa: E501

        Upload a file to OSS, which can be a video, an image and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file_to_oss(authorization, file, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param file: uploaded file (required)
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ServicesUploadFilesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_file_to_oss_with_http_info(authorization, file, **kwargs)  # noqa: E501

    def upload_file_to_oss_with_http_info(self, authorization, file, **kwargs):  # noqa: E501
        """Upload file to OSS  # noqa: E501

        Upload a file to OSS, which can be a video, an image and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file_to_oss_with_http_info(authorization, file, async_req=True)
        >>> result = thread.get()

        :param authorization: Bearer openapi_token (required)
        :type authorization: str
        :param file: uploaded file (required)
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ServicesUploadFilesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'authorization',
            'file'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file_to_oss" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and local_var_params.get('authorization') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization` when calling `upload_file_to_oss`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and local_var_params.get('file') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `upload_file_to_oss`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "ServicesUploadFilesResponse",
            500: "RainbowErrorsRainbowErrorDetailInfo",
        }

        return self.api_client.call_api(
            '/files/oss', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))