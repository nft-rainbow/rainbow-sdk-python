from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_burn_task import ModelsBurnTask
from openapi_server.models.models_burn_task_query_result import ModelsBurnTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_burn_batch_dto import ServicesBurnBatchDto
from openapi_server.models.services_burn_dto import ServicesBurnDto
from openapi_server import util


async def burn_batch(request: web.Request, authorization, burn_batch_dto) -> web.Response:
    """Batch burn NFT

    Batch burn NFT by admin

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param burn_batch_dto: burn_batch_dto
    :type burn_batch_dto: dict | bytes

    """
    burn_batch_dto = ServicesBurnBatchDto.from_dict(burn_batch_dto)
    return web.Response(status=200)


async def burn_nft(request: web.Request, authorization, burn_dto) -> web.Response:
    """Burn NFT

    Burn NFT by admin

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param burn_dto: burn_dto
    :type burn_dto: dict | bytes

    """
    burn_dto = ServicesBurnDto.from_dict(burn_dto)
    return web.Response(status=200)


async def get_burn_detail(request: web.Request, authorization, id) -> web.Response:
    """Burn NFT detail

    Get NFT Burn detail info

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def get_burn_list(request: web.Request, authorization) -> web.Response:
    """Obtain the burned NFTs list

    Get the NFT burned list information.

    :param authorization: Bearer Open_JWT
    :type authorization: str

    """
    return web.Response(status=200)
