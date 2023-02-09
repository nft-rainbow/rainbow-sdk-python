# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.middlewares_app_login import MiddlewaresAppLogin
from openapi_server.models.middlewares_login_resp import MiddlewaresLoginResp
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo


@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_login_app(client):
    """Test case for login_app

    App login
    """
    app_login_info = openapi_server.MiddlewaresAppLogin()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/login',
        headers=headers,
        json=app_login_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_refresh_auth(client):
    """Test case for refresh_auth

    Refresh JWT
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/refresh_token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

