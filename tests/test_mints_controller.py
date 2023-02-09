# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.models_mint_task import ModelsMintTask
from openapi_server.models.models_mint_task_query_result import ModelsMintTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_custom_mint_batch_dto import ServicesCustomMintBatchDto
from openapi_server.models.services_custom_mint_dto import ServicesCustomMintDto
from openapi_server.models.services_easy_mint_meta_dto import ServicesEasyMintMetaDto


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_batch_custom_mint(client):
    """Test case for batch_custom_mint

    Batch Mint NFTs
    """
    custom_mint_batch_dto = openapi_server.ServicesCustomMintBatchDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/mints/customizable/batch',
        headers=headers,
        json=custom_mint_batch_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_custom_mint(client):
    """Test case for custom_mint

    Mint NFT
    """
    custom_mint_dto = openapi_server.ServicesCustomMintDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/mints/',
        headers=headers,
        json=custom_mint_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_easy_mint_by_file(client):
    """Test case for easy_mint_by_file

    Mint NFT with file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'authorization': 'authorization_example',
    }
    data = FormData()
    data.add_field('chain', 'chain_example')
    data.add_field('description', 'description_example')
    data.add_field('mint_to_address', 'mint_to_address_example')
    data.add_field('name', 'name_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/mints/easy/files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_easy_mint_by_metadata(client):
    """Test case for easy_mint_by_metadata

    Mint NFT with metadata
    """
    easy_mint_meta_info = openapi_server.ServicesEasyMintMetaDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/mints/easy/urls',
        headers=headers,
        json=easy_mint_meta_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_mint_detail(client):
    """Test case for get_mint_detail

    Mint NFT detail
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/mints/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_mints(client):
    """Test case for list_mints

    Obtain NFT list
    """
    params = [('page', 56),
                    ('limit', 56),
                    ('contract', 'contract_example'),
                    ('mint_to', 'mint_to_example'),
                    ('status', 56),
                    ('chain', 'chain_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/mints/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

