from typing import List, Dict
from aiohttp import web

from openapi_server.models.middlewares_app_login import MiddlewaresAppLogin
from openapi_server.models.middlewares_login_resp import MiddlewaresLoginResp
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server import util


async def login_app(request: web.Request, app_login_info) -> web.Response:
    """App login

    Login the app to get the JWT according to the app_id and app_secret

    :param app_login_info: login info, contain app_id and app_secret
    :type app_login_info: dict | bytes

    """
    app_login_info = MiddlewaresAppLogin.from_dict(app_login_info)
    return web.Response(status=200)


async def refresh_auth(request: web.Request, authorization) -> web.Response:
    """Refresh JWT

    Obtain a new JWT

    :param authorization: Bearer openapi_token
    :type authorization: str

    """
    return web.Response(status=200)
