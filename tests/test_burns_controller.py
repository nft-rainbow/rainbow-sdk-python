# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.models_burn_task import ModelsBurnTask
from openapi_server.models.models_burn_task_query_result import ModelsBurnTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_burn_batch_dto import ServicesBurnBatchDto
from openapi_server.models.services_burn_dto import ServicesBurnDto


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_burn_batch(client):
    """Test case for burn_batch

    Batch burn NFT
    """
    burn_batch_dto = openapi_server.ServicesBurnBatchDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/burns/customizable/batch',
        headers=headers,
        json=burn_batch_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_burn_nft(client):
    """Test case for burn_nft

    Burn NFT
    """
    burn_dto = openapi_server.ServicesBurnDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/burns',
        headers=headers,
        json=burn_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_burn_detail(client):
    """Test case for get_burn_detail

    Burn NFT detail
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/burns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_burn_list(client):
    """Test case for get_burn_list

    Obtain the burned NFTs list
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/burns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

