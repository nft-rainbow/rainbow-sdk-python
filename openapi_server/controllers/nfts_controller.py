from typing import List, Dict
from aiohttp import web

from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_nft import ServicesNFT
from openapi_server import util


async def nft_info(request: web.Request, authorization, address, token_id) -> web.Response:
    """Get NFT info, mainly owner and metadata

    Get NFT info, mainly owner and metadata

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: address
    :type address: str
    :param token_id: token_id
    :type token_id: str

    """
    return web.Response(status=200)
