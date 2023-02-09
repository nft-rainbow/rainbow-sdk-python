from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_transfer_task import ModelsTransferTask
from openapi_server.models.models_transfer_task_query_result import ModelsTransferTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_transfer_batch_dto import ServicesTransferBatchDto
from openapi_server.models.services_transfer_dto import ServicesTransferDto
from openapi_server import util


async def batch_transfer_nft(request: web.Request, authorization, transfer_batch_dto) -> web.Response:
    """Batch Transfer NFTs

    Transfer several NFTs once

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param transfer_batch_dto: transfer_batch_dto
    :type transfer_batch_dto: dict | bytes

    """
    transfer_batch_dto = ServicesTransferBatchDto.from_dict(transfer_batch_dto)
    return web.Response(status=200)


async def get_transfer_detail(request: web.Request, authorization, id) -> web.Response:
    """Transfer NFT detail

    Get NFT Transfer detail info

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def list_transfer(request: web.Request, authorization, page=None, limit=None) -> web.Response:
    """Obtain the transferred NFTs list

    Get the NFT list containing the transferred NFT information.

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param page: page
    :type page: int
    :param limit: limit
    :type limit: int

    """
    return web.Response(status=200)


async def transfer_nft(request: web.Request, authorization, transfer_dto) -> web.Response:
    """Transfer NFT

    Transfer NFT by admin

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param transfer_dto: transfer_dto
    :type transfer_dto: dict | bytes

    """
    transfer_dto = ServicesTransferDto.from_dict(transfer_dto)
    return web.Response(status=200)
