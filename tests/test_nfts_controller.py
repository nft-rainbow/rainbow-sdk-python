# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_nft import ServicesNFT


async def test_nft_info(client):
    """Test case for nft_info

    Get NFT info, mainly owner and metadata
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/nft/{address}/{token_id}'.format(address='address_example', token_id='token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

