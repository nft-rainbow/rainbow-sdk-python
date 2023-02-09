# rainbowsdk.TransactionApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_by_id**](TransactionApi.md#get_transaction_by_id) | **GET** /tx/{id} | Get transaction informantion by ID


# **get_transaction_by_id**
> ServicesTxResp get_transaction_by_id(authorization, id)

Get transaction informantion by ID

Get transaction informantion by ID

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
    api_instance = rainbowsdk.TransactionApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
id = 'id_example' # str | Transaction ID

    try:
        # Get transaction informantion by ID
        api_response = api_instance.get_transaction_by_id(authorization, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **id** | **str**| Transaction ID | 

### Return type

[**ServicesTxResp**](ServicesTxResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction informantion |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

