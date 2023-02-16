# rainbowsdk.FilesApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_files**](FilesApi.md#list_files) | **GET** /files/ | Obtain file list
[**upload_file**](FilesApi.md#upload_file) | **POST** /files/ | Upload file
[**upload_file_to_oss**](FilesApi.md#upload_file_to_oss) | **POST** /files/oss | Upload file to OSS
[**upload_folder**](FilesApi.md#upload_folder) | **POST** /files/folder | Upload folder
[**upload_folder_to_oss**](FilesApi.md#upload_folder_to_oss) | **POST** /files/folder/oss | Upload folder to oss


# **list_files**
> ModelsFilesQueryResult list_files(authorization, page=page, limit=limit)

Obtain file list

Get the file list containing the info of the files uploaded in the specified app

### Example

```python
from __future__ import print_function
import time
import rainbowsdk
from rainbowsdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.nftrainbow.cn/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rainbowsdk.Configuration(
    host = "http://api.nftrainbow.cn/v1"
)


# Enter a context with an instance of the API client
with rainbowsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rainbowsdk.FilesApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
page = 'page_example' # str | page (optional)
limit = 'limit_example' # str | limit (optional)

    try:
        # Obtain file list
        api_response = api_instance.list_files(authorization, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **page** | **str**| page | [optional] 
 **limit** | **str**| limit | [optional] 

### Return type

[**ModelsFilesQueryResult**](ModelsFilesQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ServicesUploadFilesResponse upload_file(authorization, file)

Upload file

Upload a file which can be a video, an image and so on

### Example

```python
from __future__ import print_function
import time
import rainbowsdk
from rainbowsdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.nftrainbow.cn/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rainbowsdk.Configuration(
    host = "http://api.nftrainbow.cn/v1"
)


# Enter a context with an instance of the API client
with rainbowsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rainbowsdk.FilesApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
file = '/path/to/file' # file | uploaded file

    try:
        # Upload file
        api_response = api_instance.upload_file(authorization, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **file** | **file**| uploaded file | 

### Return type

[**ServicesUploadFilesResponse**](ServicesUploadFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_oss**
> ServicesUploadFilesResponse upload_file_to_oss(authorization, file)

Upload file to OSS

Upload a file to OSS, which can be a video, an image and so on

### Example

```python
from __future__ import print_function
import time
import rainbowsdk
from rainbowsdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.nftrainbow.cn/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rainbowsdk.Configuration(
    host = "http://api.nftrainbow.cn/v1"
)


# Enter a context with an instance of the API client
with rainbowsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rainbowsdk.FilesApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
file = '/path/to/file' # file | uploaded file

    try:
        # Upload file to OSS
        api_response = api_instance.upload_file_to_oss(authorization, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file_to_oss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **file** | **file**| uploaded file | 

### Return type

[**ServicesUploadFilesResponse**](ServicesUploadFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_folder**
> ServicesUploadFolderResponse upload_folder(authorization, folder)

Upload folder

Upload a folder containing the files which can be a video, an image and so on

### Example

```python
from __future__ import print_function
import time
import rainbowsdk
from rainbowsdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.nftrainbow.cn/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rainbowsdk.Configuration(
    host = "http://api.nftrainbow.cn/v1"
)


# Enter a context with an instance of the API client
with rainbowsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rainbowsdk.FilesApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
folder = '/path/to/file' # file | uploaded folder

    try:
        # Upload folder
        api_response = api_instance.upload_folder(authorization, folder)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **folder** | **file**| uploaded folder | 

### Return type

[**ServicesUploadFolderResponse**](ServicesUploadFolderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_folder_to_oss**
> ServicesUploadFolderResponse upload_folder_to_oss(authorization, folder)

Upload folder to oss

Upload a folder containing the files which can be a video, an image and so on, to oss

### Example

```python
from __future__ import print_function
import time
import rainbowsdk
from rainbowsdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.nftrainbow.cn/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rainbowsdk.Configuration(
    host = "http://api.nftrainbow.cn/v1"
)


# Enter a context with an instance of the API client
with rainbowsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rainbowsdk.FilesApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
folder = '/path/to/file' # file | uploaded folder

    try:
        # Upload folder to oss
        api_response = api_instance.upload_folder_to_oss(authorization, folder)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_folder_to_oss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **folder** | **file**| uploaded folder | 

### Return type

[**ServicesUploadFolderResponse**](ServicesUploadFolderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

