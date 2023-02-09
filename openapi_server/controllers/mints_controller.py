from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_mint_task import ModelsMintTask
from openapi_server.models.models_mint_task_query_result import ModelsMintTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_custom_mint_batch_dto import ServicesCustomMintBatchDto
from openapi_server.models.services_custom_mint_dto import ServicesCustomMintDto
from openapi_server.models.services_easy_mint_meta_dto import ServicesEasyMintMetaDto
from openapi_server import util


async def batch_custom_mint(request: web.Request, authorization, custom_mint_batch_dto) -> web.Response:
    """Batch Mint NFTs

    Mint several NFTs once

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param custom_mint_batch_dto: custom_mint_batch_dto
    :type custom_mint_batch_dto: dict | bytes

    """
    custom_mint_batch_dto = ServicesCustomMintBatchDto.from_dict(custom_mint_batch_dto)
    return web.Response(status=200)


async def custom_mint(request: web.Request, authorization, custom_mint_dto) -> web.Response:
    """Mint NFT

    Mint a NFT by providing a metadata url

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param custom_mint_dto: custom_mint_dto
    :type custom_mint_dto: dict | bytes

    """
    custom_mint_dto = ServicesCustomMintDto.from_dict(custom_mint_dto)
    return web.Response(status=200)


async def easy_mint_by_file(request: web.Request, authorization, chain, description, mint_to_address, name, file) -> web.Response:
    """Mint NFT with file

    Mint a NFT by uploading a file which can be a video, image and so on

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param chain: 
    :type chain: str
    :param description: 
    :type description: str
    :param mint_to_address: 
    :type mint_to_address: str
    :param name: 
    :type name: str
    :param file: file
    :type file: str

    """
    return web.Response(status=200)


async def easy_mint_by_metadata(request: web.Request, authorization, easy_mint_meta_info) -> web.Response:
    """Mint NFT with metadata

    Mint a NFT by providing a file url to create the metadata

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param easy_mint_meta_info: easy_mint_meta_info
    :type easy_mint_meta_info: dict | bytes

    """
    easy_mint_meta_info = ServicesEasyMintMetaDto.from_dict(easy_mint_meta_info)
    return web.Response(status=200)


async def get_mint_detail(request: web.Request, authorization, id) -> web.Response:
    """Mint NFT detail

    Get NFT detail info

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def list_mints(request: web.Request, authorization, page=None, limit=None, contract=None, mint_to=None, status=None, chain=None) -> web.Response:
    """Obtain NFT list

    Get the NFT list containing the NFTs minted in the specified app

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param page: page
    :type page: int
    :param limit: limit
    :type limit: int
    :param contract: contract
    :type contract: str
    :param mint_to: mint_to
    :type mint_to: str
    :param status: status
    :type status: int
    :param chain: chain
    :type chain: str

    """
    return web.Response(status=200)
