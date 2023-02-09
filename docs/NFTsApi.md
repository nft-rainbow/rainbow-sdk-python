# rainbowsdk.NFTsApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nft_info**](NFTsApi.md#nft_info) | **GET** /nft/{address}/{token_id} | Get NFT info, mainly owner and metadata


# **nft_info**
> ServicesNFT nft_info(authorization, address, token_id)

Get NFT info, mainly owner and metadata

Get NFT info, mainly owner and metadata

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
    api_instance = rainbowsdk.NFTsApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | address
token_id = 'token_id_example' # str | token_id

    try:
        # Get NFT info, mainly owner and metadata
        api_response = api_instance.nft_info(authorization, address, token_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NFTsApi->nft_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| address | 
 **token_id** | **str**| token_id | 

### Return type

[**ServicesNFT**](ServicesNFT.md)

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

