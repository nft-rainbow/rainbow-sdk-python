# rainbowsdk
The responses of the open api in swagger focus on the data field rather than the code and the message fields

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rainbowsdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rainbowsdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with rainbowsdk.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *http://api.nftrainbow.cn/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BurnsApi* | [**burn_batch**](docs/BurnsApi.md#burn_batch) | **POST** /burns/customizable/batch | Batch burn NFT
*BurnsApi* | [**burn_nft**](docs/BurnsApi.md#burn_nft) | **POST** /burns | Burn NFT
*BurnsApi* | [**get_burn_detail**](docs/BurnsApi.md#get_burn_detail) | **GET** /burns/{id} | Burn NFT detail
*BurnsApi* | [**get_burn_list**](docs/BurnsApi.md#get_burn_list) | **GET** /burns | Obtain the burned NFTs list
*ContractApi* | [**add_contract_sponsor_whitelist**](docs/ContractApi.md#add_contract_sponsor_whitelist) | **POST** /contracts/{address}/sponsor/whitelist | Add contract sponsored whitelist
*ContractApi* | [**deploy_contract**](docs/ContractApi.md#deploy_contract) | **POST** /contracts/ | Deploy contract
*ContractApi* | [**get_contract_admin**](docs/ContractApi.md#get_contract_admin) | **GET** /contracts/{address}/admin | Get administrator of contract, only work on conflux chain
*ContractApi* | [**get_contract_info**](docs/ContractApi.md#get_contract_info) | **GET** /contracts/detail/{id} | Contract detail
*ContractApi* | [**get_contract_sponsor_info**](docs/ContractApi.md#get_contract_sponsor_info) | **GET** /contracts/{address}/sponsor | Query sponsor
*ContractApi* | [**get_contract_sponsored_whitelist**](docs/ContractApi.md#get_contract_sponsored_whitelist) | **GET** /contracts/{address}/sponsor/whitelist | Get contract sponsored whitelist
*ContractApi* | [**list_contracts**](docs/ContractApi.md#list_contracts) | **GET** /contracts/ | Obtain contract list
*ContractApi* | [**remove_contract_sponsor_whitelist**](docs/ContractApi.md#remove_contract_sponsor_whitelist) | **DELETE** /contracts/{address}/sponsor/whitelist | Remove contract sponsored whitelist
*ContractApi* | [**set_contract_sponsor**](docs/ContractApi.md#set_contract_sponsor) | **POST** /contracts/{address}/sponsor | Set sponsor
*ContractApi* | [**update_contract_admin**](docs/ContractApi.md#update_contract_admin) | **PUT** /contracts/{address}/admin | Update administrator of contract
*FilesApi* | [**list_files**](docs/FilesApi.md#list_files) | **GET** /files/ | Obtain file list
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /files/ | Upload file
*FilesApi* | [**upload_file_to_oss**](docs/FilesApi.md#upload_file_to_oss) | **POST** /files/oss | Upload file to OSS
*LoginApi* | [**login_app**](docs/LoginApi.md#login_app) | **POST** /login | App login
*LoginApi* | [**refresh_auth**](docs/LoginApi.md#refresh_auth) | **GET** /refresh_token | Refresh JWT
*MetadataApi* | [**create_metadata**](docs/MetadataApi.md#create_metadata) | **POST** /metadata/ | Create NFT metadata
*MetadataApi* | [**get_metadat_info**](docs/MetadataApi.md#get_metadat_info) | **GET** /metadata/{metadata_id} | Query metadata
*MetadataApi* | [**list_metadatas**](docs/MetadataApi.md#list_metadatas) | **GET** /metadata/ | Obtain metadata list
*MintsApi* | [**batch_custom_mint**](docs/MintsApi.md#batch_custom_mint) | **POST** /mints/customizable/batch | Batch Mint NFTs
*MintsApi* | [**custom_mint**](docs/MintsApi.md#custom_mint) | **POST** /mints/ | Mint NFT
*MintsApi* | [**easy_mint_by_file**](docs/MintsApi.md#easy_mint_by_file) | **POST** /mints/easy/files | Mint NFT with file
*MintsApi* | [**easy_mint_by_metadata**](docs/MintsApi.md#easy_mint_by_metadata) | **POST** /mints/easy/urls | Mint NFT with metadata
*MintsApi* | [**get_mint_detail**](docs/MintsApi.md#get_mint_detail) | **GET** /mints/{id} | Mint NFT detail
*MintsApi* | [**list_mints**](docs/MintsApi.md#list_mints) | **GET** /mints/ | Obtain NFT list
*NFTsApi* | [**nft_info**](docs/NFTsApi.md#nft_info) | **GET** /nft/{address}/{token_id} | Get NFT info, mainly owner and metadata
*TransactionApi* | [**get_transaction_by_id**](docs/TransactionApi.md#get_transaction_by_id) | **GET** /tx/{id} | Get transaction informantion by ID
*TransfersApi* | [**batch_transfer_nft**](docs/TransfersApi.md#batch_transfer_nft) | **POST** /transfers/customizable/batch | Batch Transfer NFTs
*TransfersApi* | [**get_transfer_detail**](docs/TransfersApi.md#get_transfer_detail) | **GET** /transfers/{id} | Transfer NFT detail
*TransfersApi* | [**list_transfer**](docs/TransfersApi.md#list_transfer) | **GET** /transfers/ | Obtain the transferred NFTs list
*TransfersApi* | [**transfer_nft**](docs/TransfersApi.md#transfer_nft) | **POST** /transfers/customizable | Transfer NFT


## Documentation For Models

 - [GormDeletedAt](docs/GormDeletedAt.md)
 - [MiddlewaresAppLogin](docs/MiddlewaresAppLogin.md)
 - [MiddlewaresLoginResp](docs/MiddlewaresLoginResp.md)
 - [ModelsBurnTask](docs/ModelsBurnTask.md)
 - [ModelsBurnTaskQueryResult](docs/ModelsBurnTaskQueryResult.md)
 - [ModelsContract](docs/ModelsContract.md)
 - [ModelsContractTaskQueryResult](docs/ModelsContractTaskQueryResult.md)
 - [ModelsExposedFile](docs/ModelsExposedFile.md)
 - [ModelsExposedMetadata](docs/ModelsExposedMetadata.md)
 - [ModelsExposedMetadataAttribute](docs/ModelsExposedMetadataAttribute.md)
 - [ModelsExposedMetadataQueryResult](docs/ModelsExposedMetadataQueryResult.md)
 - [ModelsFilesQueryResult](docs/ModelsFilesQueryResult.md)
 - [ModelsMintTask](docs/ModelsMintTask.md)
 - [ModelsMintTaskQueryResult](docs/ModelsMintTaskQueryResult.md)
 - [ModelsTransferTask](docs/ModelsTransferTask.md)
 - [ModelsTransferTaskQueryResult](docs/ModelsTransferTaskQueryResult.md)
 - [MultipartFileHeader](docs/MultipartFileHeader.md)
 - [RainbowErrorsRainbowErrorDetailInfo](docs/RainbowErrorsRainbowErrorDetailInfo.md)
 - [ServicesBurnBatchDto](docs/ServicesBurnBatchDto.md)
 - [ServicesBurnDto](docs/ServicesBurnDto.md)
 - [ServicesBurnItemDto](docs/ServicesBurnItemDto.md)
 - [ServicesContractAdminUpdateDto](docs/ServicesContractAdminUpdateDto.md)
 - [ServicesContractDeployDto](docs/ServicesContractDeployDto.md)
 - [ServicesCustomMintBatchDto](docs/ServicesCustomMintBatchDto.md)
 - [ServicesCustomMintDto](docs/ServicesCustomMintDto.md)
 - [ServicesEasyMintMetaDto](docs/ServicesEasyMintMetaDto.md)
 - [ServicesMetadataDto](docs/ServicesMetadataDto.md)
 - [ServicesMintItemDto](docs/ServicesMintItemDto.md)
 - [ServicesNFT](docs/ServicesNFT.md)
 - [ServicesSendTxResp](docs/ServicesSendTxResp.md)
 - [ServicesSetSponsorResp](docs/ServicesSetSponsorResp.md)
 - [ServicesSponsorInfo](docs/ServicesSponsorInfo.md)
 - [ServicesTransferBatchDto](docs/ServicesTransferBatchDto.md)
 - [ServicesTransferDto](docs/ServicesTransferDto.md)
 - [ServicesTransferItemDto](docs/ServicesTransferItemDto.md)
 - [ServicesTxResp](docs/ServicesTxResp.md)
 - [ServicesUploadFilesResponse](docs/ServicesUploadFilesResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




