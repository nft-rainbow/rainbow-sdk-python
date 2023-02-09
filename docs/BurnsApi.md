# rainbowsdk.BurnsApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**burn_batch**](BurnsApi.md#burn_batch) | **POST** /burns/customizable/batch | Batch burn NFT
[**burn_nft**](BurnsApi.md#burn_nft) | **POST** /burns | Burn NFT
[**get_burn_detail**](BurnsApi.md#get_burn_detail) | **GET** /burns/{id} | Burn NFT detail
[**get_burn_list**](BurnsApi.md#get_burn_list) | **GET** /burns | Obtain the burned NFTs list


# **burn_batch**
> list[ModelsBurnTask] burn_batch(authorization, burn_batch_dto)

Batch burn NFT

Batch burn NFT by admin

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
    api_instance = rainbowsdk.BurnsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
burn_batch_dto = rainbowsdk.ServicesBurnBatchDto() # ServicesBurnBatchDto | burn_batch_dto

    try:
        # Batch burn NFT
        api_response = api_instance.burn_batch(authorization, burn_batch_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BurnsApi->burn_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **burn_batch_dto** | [**ServicesBurnBatchDto**](ServicesBurnBatchDto.md)| burn_batch_dto | 

### Return type

[**list[ModelsBurnTask]**](ModelsBurnTask.md)

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

# **burn_nft**
> ModelsBurnTask burn_nft(authorization, burn_dto)

Burn NFT

Burn NFT by admin

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
    api_instance = rainbowsdk.BurnsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
burn_dto = rainbowsdk.ServicesBurnDto() # ServicesBurnDto | burn_dto

    try:
        # Burn NFT
        api_response = api_instance.burn_nft(authorization, burn_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BurnsApi->burn_nft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **burn_dto** | [**ServicesBurnDto**](ServicesBurnDto.md)| burn_dto | 

### Return type

[**ModelsBurnTask**](ModelsBurnTask.md)

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

# **get_burn_detail**
> ModelsBurnTask get_burn_detail(authorization, id)

Burn NFT detail

Get NFT Burn detail info

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
    api_instance = rainbowsdk.BurnsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
id = 56 # int | id

    try:
        # Burn NFT detail
        api_response = api_instance.get_burn_detail(authorization, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BurnsApi->get_burn_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **id** | **int**| id | 

### Return type

[**ModelsBurnTask**](ModelsBurnTask.md)

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

# **get_burn_list**
> ModelsBurnTaskQueryResult get_burn_list(authorization)

Obtain the burned NFTs list

Get the NFT burned list information.

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
    api_instance = rainbowsdk.BurnsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT

    try:
        # Obtain the burned NFTs list
        api_response = api_instance.get_burn_list(authorization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BurnsApi->get_burn_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 

### Return type

[**ModelsBurnTaskQueryResult**](ModelsBurnTaskQueryResult.md)

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

