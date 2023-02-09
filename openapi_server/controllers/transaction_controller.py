from typing import List, Dict
from aiohttp import web

from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_tx_resp import ServicesTxResp
from openapi_server import util


async def get_transaction_by_id(request: web.Request, authorization, id) -> web.Response:
    """Get transaction informantion by ID

    Get transaction informantion by ID

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param id: Transaction ID
    :type id: str

    """
    return web.Response(status=200)
