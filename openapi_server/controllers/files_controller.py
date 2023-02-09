from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_files_query_result import ModelsFilesQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_upload_files_response import ServicesUploadFilesResponse
from openapi_server import util


async def list_files(request: web.Request, authorization, page=None, limit=None) -> web.Response:
    """Obtain file list

    Get the file list containing the info of the files uploaded in the specified app

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param page: page
    :type page: str
    :param limit: limit
    :type limit: str

    """
    return web.Response(status=200)


async def upload_file(request: web.Request, authorization, file) -> web.Response:
    """Upload file

    Upload a file which can be a video, an image and so on

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param file: uploaded file
    :type file: str

    """
    return web.Response(status=200)


async def upload_file_to_oss(request: web.Request, authorization, file) -> web.Response:
    """Upload file to OSS

    Upload a file to OSS, which can be a video, an image and so on

    :param authorization: Bearer openapi_token
    :type authorization: str
    :param file: uploaded file
    :type file: str

    """
    return web.Response(status=200)
