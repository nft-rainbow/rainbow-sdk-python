# rainbowsdk.LoginApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_app**](LoginApi.md#login_app) | **POST** /login | App login
[**refresh_auth**](LoginApi.md#refresh_auth) | **GET** /refresh_token | Refresh JWT


# **login_app**
> MiddlewaresLoginResp login_app(app_login_info)

App login

Login the app to get the JWT according to the app_id and app_secret

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
    api_instance = rainbowsdk.LoginApi(api_client)
    app_login_info = rainbowsdk.MiddlewaresAppLoginInfo() # MiddlewaresAppLoginInfo | login info, contain app_id and app_secret

    try:
        # App login
        api_response = api_instance.login_app(app_login_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoginApi->login_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_login_info** | [**MiddlewaresAppLoginInfo**](MiddlewaresAppLoginInfo.md)| login info, contain app_id and app_secret | 

### Return type

[**MiddlewaresLoginResp**](MiddlewaresLoginResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | auth token |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> MiddlewaresLoginResp refresh_auth(authorization)

Refresh JWT

Obtain a new JWT

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
    api_instance = rainbowsdk.LoginApi(api_client)
    authorization = 'authorization_example' # str | Bearer openapi_token

    try:
        # Refresh JWT
        api_response = api_instance.refresh_auth(authorization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoginApi->refresh_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer openapi_token | 

### Return type

[**MiddlewaresLoginResp**](MiddlewaresLoginResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | refreshed auth token |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

