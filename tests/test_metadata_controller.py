# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.models_exposed_metadata import ModelsExposedMetadata
from openapi_server.models.models_exposed_metadata_query_result import ModelsExposedMetadataQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_metadata_dto import ServicesMetadataDto


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_metadata(client):
    """Test case for create_metadata

    Create NFT metadata
    """
    metadata_info = openapi_server.ServicesMetadataDto()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/metadata/',
        headers=headers,
        json=metadata_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_metadat_info(client):
    """Test case for get_metadat_info

    Query metadata
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/metadata/{metadata_id}'.format(metadata_id='metadata_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_metadatas(client):
    """Test case for list_metadatas

    Obtain metadata list
    """
    params = [('page', 'page_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/metadata/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

