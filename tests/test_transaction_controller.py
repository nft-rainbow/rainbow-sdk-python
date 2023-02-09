# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_tx_resp import ServicesTxResp


async def test_get_transaction_by_id(client):
    """Test case for get_transaction_by_id

    Get transaction informantion by ID
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/tx/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

