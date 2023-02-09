# rainbowsdk.MintsApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_custom_mint**](MintsApi.md#batch_custom_mint) | **POST** /mints/customizable/batch | Batch Mint NFTs
[**custom_mint**](MintsApi.md#custom_mint) | **POST** /mints/ | Mint NFT
[**easy_mint_by_file**](MintsApi.md#easy_mint_by_file) | **POST** /mints/easy/files | Mint NFT with file
[**easy_mint_by_metadata**](MintsApi.md#easy_mint_by_metadata) | **POST** /mints/easy/urls | Mint NFT with metadata
[**get_mint_detail**](MintsApi.md#get_mint_detail) | **GET** /mints/{id} | Mint NFT detail
[**list_mints**](MintsApi.md#list_mints) | **GET** /mints/ | Obtain NFT list


# **batch_custom_mint**
> list[ModelsMintTask] batch_custom_mint(authorization, custom_mint_batch_dto)

Batch Mint NFTs

Mint several NFTs once

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
custom_mint_batch_dto = rainbowsdk.ServicesCustomMintBatchDto() # ServicesCustomMintBatchDto | custom_mint_batch_dto

    try:
        # Batch Mint NFTs
        api_response = api_instance.batch_custom_mint(authorization, custom_mint_batch_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->batch_custom_mint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **custom_mint_batch_dto** | [**ServicesCustomMintBatchDto**](ServicesCustomMintBatchDto.md)| custom_mint_batch_dto | 

### Return type

[**list[ModelsMintTask]**](ModelsMintTask.md)

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

# **custom_mint**
> ModelsMintTask custom_mint(authorization, custom_mint_dto)

Mint NFT

Mint a NFT by providing a metadata url

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
custom_mint_dto = rainbowsdk.ServicesCustomMintDto() # ServicesCustomMintDto | custom_mint_dto

    try:
        # Mint NFT
        api_response = api_instance.custom_mint(authorization, custom_mint_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->custom_mint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **custom_mint_dto** | [**ServicesCustomMintDto**](ServicesCustomMintDto.md)| custom_mint_dto | 

### Return type

[**ModelsMintTask**](ModelsMintTask.md)

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

# **easy_mint_by_file**
> ModelsMintTask easy_mint_by_file(authorization, chain, description, mint_to_address, name, file)

Mint NFT with file

Mint a NFT by uploading a file which can be a video, image and so on

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
chain = 'chain_example' # str | 
description = 'description_example' # str | 
mint_to_address = 'mint_to_address_example' # str | 
name = 'name_example' # str | 
file = '/path/to/file' # file | file

    try:
        # Mint NFT with file
        api_response = api_instance.easy_mint_by_file(authorization, chain, description, mint_to_address, name, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->easy_mint_by_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **chain** | **str**|  | 
 **description** | **str**|  | 
 **mint_to_address** | **str**|  | 
 **name** | **str**|  | 
 **file** | **file**| file | 

### Return type

[**ModelsMintTask**](ModelsMintTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_mint_by_metadata**
> ModelsMintTask easy_mint_by_metadata(authorization, easy_mint_meta_info)

Mint NFT with metadata

Mint a NFT by providing a file url to create the metadata

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
easy_mint_meta_info = rainbowsdk.ServicesEasyMintMetaDto() # ServicesEasyMintMetaDto | easy_mint_meta_info

    try:
        # Mint NFT with metadata
        api_response = api_instance.easy_mint_by_metadata(authorization, easy_mint_meta_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->easy_mint_by_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **easy_mint_meta_info** | [**ServicesEasyMintMetaDto**](ServicesEasyMintMetaDto.md)| easy_mint_meta_info | 

### Return type

[**ModelsMintTask**](ModelsMintTask.md)

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

# **get_mint_detail**
> ModelsMintTask get_mint_detail(authorization, id)

Mint NFT detail

Get NFT detail info

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
id = 56 # int | id

    try:
        # Mint NFT detail
        api_response = api_instance.get_mint_detail(authorization, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->get_mint_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **id** | **int**| id | 

### Return type

[**ModelsMintTask**](ModelsMintTask.md)

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

# **list_mints**
> ModelsMintTaskQueryResult list_mints(authorization, page=page, limit=limit, contract=contract, mint_to=mint_to, status=status, chain=chain)

Obtain NFT list

Get the NFT list containing the NFTs minted in the specified app

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
    api_instance = rainbowsdk.MintsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
page = 56 # int | page (optional)
limit = 56 # int | limit (optional)
contract = 'contract_example' # str | contract (optional)
mint_to = 'mint_to_example' # str | mint_to (optional)
status = 56 # int | status (optional)
chain = 'chain_example' # str | chain (optional)

    try:
        # Obtain NFT list
        api_response = api_instance.list_mints(authorization, page=page, limit=limit, contract=contract, mint_to=mint_to, status=status, chain=chain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MintsApi->list_mints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **page** | **int**| page | [optional] 
 **limit** | **int**| limit | [optional] 
 **contract** | **str**| contract | [optional] 
 **mint_to** | **str**| mint_to | [optional] 
 **status** | **int**| status | [optional] 
 **chain** | **str**| chain | [optional] 

### Return type

[**ModelsMintTaskQueryResult**](ModelsMintTaskQueryResult.md)

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

