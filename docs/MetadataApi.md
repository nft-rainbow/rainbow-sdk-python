# rainbowsdk.MetadataApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata**](MetadataApi.md#create_metadata) | **POST** /metadata/ | Create NFT metadata
[**get_metadat_info**](MetadataApi.md#get_metadat_info) | **GET** /metadata/{metadata_id} | Query metadata
[**list_metadatas**](MetadataApi.md#list_metadatas) | **GET** /metadata/ | Obtain metadata list


# **create_metadata**
> ModelsExposedMetadata create_metadata(authorization, metadata_info)

Create NFT metadata

Create NFT metadata by providing the info including name, description and so on

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
    api_instance = rainbowsdk.MetadataApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
metadata_info = rainbowsdk.ServicesMetadataDto() # ServicesMetadataDto | metadata_info

    try:
        # Create NFT metadata
        api_response = api_instance.create_metadata(authorization, metadata_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->create_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **metadata_info** | [**ServicesMetadataDto**](ServicesMetadataDto.md)| metadata_info | 

### Return type

[**ModelsExposedMetadata**](ModelsExposedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadat_info**
> ModelsExposedMetadata get_metadat_info(authorization, metadata_id)

Query metadata

Query the metadata according to metadata_id

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
    api_instance = rainbowsdk.MetadataApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
metadata_id = 'metadata_id_example' # str | metadata_id

    try:
        # Query metadata
        api_response = api_instance.get_metadat_info(authorization, metadata_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->get_metadat_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **metadata_id** | **str**| metadata_id | 

### Return type

[**ModelsExposedMetadata**](ModelsExposedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadatas**
> ModelsExposedMetadataQueryResult list_metadatas(authorization, page=page, limit=limit)

Obtain metadata list

Get the metadata list containing the info of the metadata created in the specified app

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
    api_instance = rainbowsdk.MetadataApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token
page = 'page_example' # str | page (optional)
limit = 'limit_example' # str | limit (optional)

    try:
        # Obtain metadata list
        api_response = api_instance.list_metadatas(authorization, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->list_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 
 **page** | **str**| page | [optional] 
 **limit** | **str**| limit | [optional] 

### Return type

[**ModelsExposedMetadataQueryResult**](ModelsExposedMetadataQueryResult.md)

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

