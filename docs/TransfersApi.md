# rainbowsdk.TransfersApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_transfer_nft**](TransfersApi.md#batch_transfer_nft) | **POST** /transfers/customizable/batch | Batch Transfer NFTs
[**get_transfer_detail**](TransfersApi.md#get_transfer_detail) | **GET** /transfers/{id} | Transfer NFT detail
[**list_transfer**](TransfersApi.md#list_transfer) | **GET** /transfers/ | Obtain the transferred NFTs list
[**transfer_nft**](TransfersApi.md#transfer_nft) | **POST** /transfers/customizable | Transfer NFT


# **batch_transfer_nft**
> list[ModelsTransferTask] batch_transfer_nft(authorization, transfer_batch_dto)

Batch Transfer NFTs

Transfer several NFTs once

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
    api_instance = rainbowsdk.TransfersApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
transfer_batch_dto = rainbowsdk.ServicesTransferBatchDto() # ServicesTransferBatchDto | transfer_batch_dto

    try:
        # Batch Transfer NFTs
        api_response = api_instance.batch_transfer_nft(authorization, transfer_batch_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->batch_transfer_nft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **transfer_batch_dto** | [**ServicesTransferBatchDto**](ServicesTransferBatchDto.md)| transfer_batch_dto | 

### Return type

[**list[ModelsTransferTask]**](ModelsTransferTask.md)

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

# **get_transfer_detail**
> ModelsTransferTask get_transfer_detail(authorization, id)

Transfer NFT detail

Get NFT Transfer detail info

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
    api_instance = rainbowsdk.TransfersApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
id = 56 # int | id

    try:
        # Transfer NFT detail
        api_response = api_instance.get_transfer_detail(authorization, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->get_transfer_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **id** | **int**| id | 

### Return type

[**ModelsTransferTask**](ModelsTransferTask.md)

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

# **list_transfer**
> ModelsTransferTaskQueryResult list_transfer(authorization, page=page, limit=limit)

Obtain the transferred NFTs list

Get the NFT list containing the transferred NFT information.

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
    api_instance = rainbowsdk.TransfersApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
page = 56 # int | page (optional)
limit = 56 # int | limit (optional)

    try:
        # Obtain the transferred NFTs list
        api_response = api_instance.list_transfer(authorization, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->list_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **page** | **int**| page | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**ModelsTransferTaskQueryResult**](ModelsTransferTaskQueryResult.md)

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

# **transfer_nft**
> ModelsTransferTask transfer_nft(authorization, transfer_dto)

Transfer NFT

Transfer NFT by admin

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
    api_instance = rainbowsdk.TransfersApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
transfer_dto = rainbowsdk.ServicesTransferDto() # ServicesTransferDto | transfer_dto

    try:
        # Transfer NFT
        api_response = api_instance.transfer_nft(authorization, transfer_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->transfer_nft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **transfer_dto** | [**ServicesTransferDto**](ServicesTransferDto.md)| transfer_dto | 

### Return type

[**ModelsTransferTask**](ModelsTransferTask.md)

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

