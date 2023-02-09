# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.models_transfer_task import ModelsTransferTask
from openapi_server.models.models_transfer_task_query_result import ModelsTransferTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_transfer_batch_dto import ServicesTransferBatchDto
from openapi_server.models.services_transfer_dto import ServicesTransferDto


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_batch_transfer_nft(client):
    """Test case for batch_transfer_nft

    Batch Transfer NFTs
    """
    transfer_batch_dto = openapi_server.ServicesTransferBatchDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/transfers/customizable/batch',
        headers=headers,
        json=transfer_batch_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_transfer_detail(client):
    """Test case for get_transfer_detail

    Transfer NFT detail
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/transfers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_transfer(client):
    """Test case for list_transfer

    Obtain the transferred NFTs list
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/transfers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_transfer_nft(client):
    """Test case for transfer_nft

    Transfer NFT
    """
    transfer_dto = openapi_server.ServicesTransferDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/transfers/customizable',
        headers=headers,
        json=transfer_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

