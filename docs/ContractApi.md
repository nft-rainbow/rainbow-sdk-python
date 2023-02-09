# rainbowsdk.ContractApi

All URIs are relative to *http://api.nftrainbow.cn/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contract_sponsor_whitelist**](ContractApi.md#add_contract_sponsor_whitelist) | **POST** /contracts/{address}/sponsor/whitelist | Add contract sponsored whitelist
[**deploy_contract**](ContractApi.md#deploy_contract) | **POST** /contracts/ | Deploy contract
[**get_contract_admin**](ContractApi.md#get_contract_admin) | **GET** /contracts/{address}/admin | Get administrator of contract, only work on conflux chain
[**get_contract_info**](ContractApi.md#get_contract_info) | **GET** /contracts/detail/{id} | Contract detail
[**get_contract_sponsor_info**](ContractApi.md#get_contract_sponsor_info) | **GET** /contracts/{address}/sponsor | Query sponsor
[**get_contract_sponsored_whitelist**](ContractApi.md#get_contract_sponsored_whitelist) | **GET** /contracts/{address}/sponsor/whitelist | Get contract sponsored whitelist
[**list_contracts**](ContractApi.md#list_contracts) | **GET** /contracts/ | Obtain contract list
[**remove_contract_sponsor_whitelist**](ContractApi.md#remove_contract_sponsor_whitelist) | **DELETE** /contracts/{address}/sponsor/whitelist | Remove contract sponsored whitelist
[**set_contract_sponsor**](ContractApi.md#set_contract_sponsor) | **POST** /contracts/{address}/sponsor | Set sponsor
[**update_contract_admin**](ContractApi.md#update_contract_admin) | **PUT** /contracts/{address}/admin | Update administrator of contract


# **add_contract_sponsor_whitelist**
> ServicesSendTxResp add_contract_sponsor_whitelist(authorization, address, users)

Add contract sponsored whitelist

Add contract sponsored whitelist, only work on conflux chain

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | contract address
users = ['users_example'] # list[str] | Adding sponsor whitelist

    try:
        # Add contract sponsored whitelist
        api_response = api_instance.add_contract_sponsor_whitelist(authorization, address, users)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->add_contract_sponsor_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| contract address | 
 **users** | [**list[str]**](str.md)| Adding sponsor whitelist | 

### Return type

[**ServicesSendTxResp**](ServicesSendTxResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction id |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_contract**
> ModelsContract deploy_contract(authorization, contract_info)

Deploy contract

Deploy a ERC721 or ERC1155 contract.

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
contract_info = rainbowsdk.ServicesContractDeployDto() # ServicesContractDeployDto | contract_info

    try:
        # Deploy contract
        api_response = api_instance.deploy_contract(authorization, contract_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->deploy_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **contract_info** | [**ServicesContractDeployDto**](ServicesContractDeployDto.md)| contract_info | 

### Return type

[**ModelsContract**](ModelsContract.md)

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

# **get_contract_admin**
> str get_contract_admin(authorization, address)

Get administrator of contract, only work on conflux chain

Get Contract Admin

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | contract address

    try:
        # Get administrator of contract, only work on conflux chain
        api_response = api_instance.get_contract_admin(authorization, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->get_contract_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| contract address | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Admin address |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_info**
> ModelsContract get_contract_info(authorization, id)

Contract detail

Get Contract info

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
id = 56 # int | id

    try:
        # Contract detail
        api_response = api_instance.get_contract_info(authorization, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->get_contract_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **id** | **int**| id | 

### Return type

[**ModelsContract**](ModelsContract.md)

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

# **get_contract_sponsor_info**
> ServicesSponsorInfo get_contract_sponsor_info(authorization, address, chain=chain)

Query sponsor

Get the sponsor of the specified contract according to address.

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | address
chain = 'chain_example' # str | chain (optional)

    try:
        # Query sponsor
        api_response = api_instance.get_contract_sponsor_info(authorization, address, chain=chain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->get_contract_sponsor_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| address | 
 **chain** | **str**| chain | [optional] 

### Return type

[**ServicesSponsorInfo**](ServicesSponsorInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid address |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_sponsored_whitelist**
> list[str] get_contract_sponsored_whitelist(authorization, address)

Get contract sponsored whitelist

Get contract sponsored whitelist, only work on conflux chain

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | contract address

    try:
        # Get contract sponsored whitelist
        api_response = api_instance.get_contract_sponsored_whitelist(authorization, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->get_contract_sponsored_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| contract address | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract sponsored whitelist |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contracts**
> ModelsContractTaskQueryResult list_contracts(authorization, page=page, limit=limit)

Obtain contract list

Get the contract list containing the contracts deployed through the specified app.

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
page = 56 # int | page (optional)
limit = 56 # int | limit (optional)

    try:
        # Obtain contract list
        api_response = api_instance.list_contracts(authorization, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->list_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **page** | **int**| page | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**ModelsContractTaskQueryResult**](ModelsContractTaskQueryResult.md)

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

# **remove_contract_sponsor_whitelist**
> ServicesSendTxResp remove_contract_sponsor_whitelist(authorization, address, users)

Remove contract sponsored whitelist

Remove contract sponsored whitelist, only work on conflux chain

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | contract address
users = ['users_example'] # list[str] | Removing sponsor whitelist

    try:
        # Remove contract sponsored whitelist
        api_response = api_instance.remove_contract_sponsor_whitelist(authorization, address, users)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->remove_contract_sponsor_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| contract address | 
 **users** | [**list[str]**](str.md)| Removing sponsor whitelist | 

### Return type

[**ServicesSendTxResp**](ServicesSendTxResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction id |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_contract_sponsor**
> ServicesSetSponsorResp set_contract_sponsor(authorization, address, chain=chain, auto_sponsor=auto_sponsor)

Set sponsor

Set the sponsor for a contract according to the address with specified value(gas-1, storage-50)

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | Contract address
chain = 'chain_example' # str | chain (optional)
auto_sponsor = True # bool | Open auto sponsor or not, for mainnet contract keep user account have enough balance (optional)

    try:
        # Set sponsor
        api_response = api_instance.set_contract_sponsor(authorization, address, chain=chain, auto_sponsor=auto_sponsor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->set_contract_sponsor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| Contract address | 
 **chain** | **str**| chain | [optional] 
 **auto_sponsor** | **bool**| Open auto sponsor or not, for mainnet contract keep user account have enough balance | [optional] 

### Return type

[**ServicesSetSponsorResp**](ServicesSetSponsorResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction id\&quot; \&quot;success |  -  |
**400** | Invalid address |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract_admin**
> ServicesSendTxResp update_contract_admin(authorization, address, admin_info)

Update administrator of contract

Update administrator of contract, only work on conflux chain

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
    api_instance = rainbowsdk.ContractApi(api_client)
    authorization = 'authorization_example' # str | Bearer Open_JWT
address = 'address_example' # str | contract address
admin_info = rainbowsdk.ServicesContractAdminUpdateDto() # ServicesContractAdminUpdateDto | contract admin update info

    try:
        # Update administrator of contract
        api_response = api_instance.update_contract_admin(authorization, address, admin_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->update_contract_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer Open_JWT | 
 **address** | **str**| contract address | 
 **admin_info** | [**ServicesContractAdminUpdateDto**](ServicesContractAdminUpdateDto.md)| contract admin update info | 

### Return type

[**ServicesSendTxResp**](ServicesSendTxResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction id |  -  |
**400** | Invalid request |  -  |
**500** | Internal Server error |  -  |
**599** | Businesss error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

