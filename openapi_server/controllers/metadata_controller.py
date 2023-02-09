from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_exposed_metadata import ModelsExposedMetadata
from openapi_server.models.models_exposed_metadata_query_result import ModelsExposedMetadataQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_metadata_dto import ServicesMetadataDto
from openapi_server import util


async def create_metadata(request: web.Request, authorization, metadata_info) -> web.Response:
    """Create NFT metadata

    Create NFT metadata by providing the info including name, description and so on

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param metadata_info: metadata_info
    :type metadata_info: dict | bytes

    """
    metadata_info = ServicesMetadataDto.from_dict(metadata_info)
    return web.Response(status=200)


async def get_metadat_info(request: web.Request, authorization, metadata_id) -> web.Response:
    """Query metadata

    Query the metadata according to metadata_id

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param metadata_id: metadata_id
    :type metadata_id: str

    """
    return web.Response(status=200)


async def list_metadatas(request: web.Request, authorization, page=None, limit=None) -> web.Response:
    """Obtain metadata list

    Get the metadata list containing the info of the metadata created in the specified app

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param page: page
    :type page: str
    :param limit: limit
    :type limit: str

    """
    return web.Response(status=200)
