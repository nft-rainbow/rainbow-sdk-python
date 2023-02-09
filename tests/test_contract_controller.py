# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.models_contract import ModelsContract
from openapi_server.models.models_contract_task_query_result import ModelsContractTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_contract_admin_update_dto import ServicesContractAdminUpdateDto
from openapi_server.models.services_contract_deploy_dto import ServicesContractDeployDto
from openapi_server.models.services_send_tx_resp import ServicesSendTxResp
from openapi_server.models.services_set_sponsor_resp import ServicesSetSponsorResp
from openapi_server.models.services_sponsor_info import ServicesSponsorInfo


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_contract_sponsor_whitelist(client):
    """Test case for add_contract_sponsor_whitelist

    Add contract sponsored whitelist
    """
    users = ['users_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/contracts/{address}/sponsor/whitelist'.format(address='address_example'),
        headers=headers,
        json=users,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_deploy_contract(client):
    """Test case for deploy_contract

    Deploy contract
    """
    contract_info = openapi_server.ServicesContractDeployDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/contracts/',
        headers=headers,
        json=contract_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_contract_admin(client):
    """Test case for get_contract_admin

    Get administrator of contract, only work on conflux chain
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/contracts/{address}/admin'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_contract_info(client):
    """Test case for get_contract_info

    Contract detail
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/contracts/detail/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_contract_sponsor_info(client):
    """Test case for get_contract_sponsor_info

    Query sponsor
    """
    params = [('chain', 'chain_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/contracts/{address}/sponsor'.format(address='address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_contract_sponsored_whitelist(client):
    """Test case for get_contract_sponsored_whitelist

    Get contract sponsored whitelist
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/contracts/{address}/sponsor/whitelist'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_contracts(client):
    """Test case for list_contracts

    Obtain contract list
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/contracts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remove_contract_sponsor_whitelist(client):
    """Test case for remove_contract_sponsor_whitelist

    Remove contract sponsored whitelist
    """
    users = ['users_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/contracts/{address}/sponsor/whitelist'.format(address='address_example'),
        headers=headers,
        json=users,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_set_contract_sponsor(client):
    """Test case for set_contract_sponsor

    Set sponsor
    """
    params = [('chain', 'chain_example'),
                    ('auto_sponsor', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/contracts/{address}/sponsor'.format(address='address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_contract_admin(client):
    """Test case for update_contract_admin

    Update administrator of contract
    """
    admin_info = openapi_server.ServicesContractAdminUpdateDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/v1/contracts/{address}/admin'.format(address='address_example'),
        headers=headers,
        json=admin_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

