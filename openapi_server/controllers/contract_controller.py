from typing import List, Dict
from aiohttp import web

from openapi_server.models.models_contract import ModelsContract
from openapi_server.models.models_contract_task_query_result import ModelsContractTaskQueryResult
from openapi_server.models.rainbow_errors_rainbow_error_detail_info import RainbowErrorsRainbowErrorDetailInfo
from openapi_server.models.services_contract_admin_update_dto import ServicesContractAdminUpdateDto
from openapi_server.models.services_contract_deploy_dto import ServicesContractDeployDto
from openapi_server.models.services_send_tx_resp import ServicesSendTxResp
from openapi_server.models.services_set_sponsor_resp import ServicesSetSponsorResp
from openapi_server.models.services_sponsor_info import ServicesSponsorInfo
from openapi_server import util


async def add_contract_sponsor_whitelist(request: web.Request, authorization, address, users) -> web.Response:
    """Add contract sponsored whitelist

    Add contract sponsored whitelist, only work on conflux chain

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: contract address
    :type address: str
    :param users: Adding sponsor whitelist
    :type users: List[str]

    """
    return web.Response(status=200)


async def deploy_contract(request: web.Request, authorization, contract_info) -> web.Response:
    """Deploy contract

    Deploy a ERC721 or ERC1155 contract.

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param contract_info: contract_info
    :type contract_info: dict | bytes

    """
    contract_info = ServicesContractDeployDto.from_dict(contract_info)
    return web.Response(status=200)


async def get_contract_admin(request: web.Request, authorization, address) -> web.Response:
    """Get administrator of contract, only work on conflux chain

    Get Contract Admin

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: contract address
    :type address: str

    """
    return web.Response(status=200)


async def get_contract_info(request: web.Request, authorization, id) -> web.Response:
    """Contract detail

    Get Contract info

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def get_contract_sponsor_info(request: web.Request, authorization, address, chain=None) -> web.Response:
    """Query sponsor

    Get the sponsor of the specified contract according to address.

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: address
    :type address: str
    :param chain: chain
    :type chain: str

    """
    return web.Response(status=200)


async def get_contract_sponsored_whitelist(request: web.Request, authorization, address) -> web.Response:
    """Get contract sponsored whitelist

    Get contract sponsored whitelist, only work on conflux chain

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: contract address
    :type address: str

    """
    return web.Response(status=200)


async def list_contracts(request: web.Request, authorization, page=None, limit=None) -> web.Response:
    """Obtain contract list

    Get the contract list containing the contracts deployed through the specified app.

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param page: page
    :type page: int
    :param limit: limit
    :type limit: int

    """
    return web.Response(status=200)


async def remove_contract_sponsor_whitelist(request: web.Request, authorization, address, users) -> web.Response:
    """Remove contract sponsored whitelist

    Remove contract sponsored whitelist, only work on conflux chain

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: contract address
    :type address: str
    :param users: Removing sponsor whitelist
    :type users: List[str]

    """
    return web.Response(status=200)


async def set_contract_sponsor(request: web.Request, authorization, address, chain=None, auto_sponsor=None) -> web.Response:
    """Set sponsor

    Set the sponsor for a contract according to the address with specified value(gas-1, storage-50)

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: Contract address
    :type address: str
    :param chain: chain
    :type chain: str
    :param auto_sponsor: Open auto sponsor or not, for mainnet contract keep user account have enough balance
    :type auto_sponsor: bool

    """
    return web.Response(status=200)


async def update_contract_admin(request: web.Request, authorization, address, admin_info) -> web.Response:
    """Update administrator of contract

    Update administrator of contract, only work on conflux chain

    :param authorization: Bearer Open_JWT
    :type authorization: str
    :param address: contract address
    :type address: str
    :param admin_info: contract admin update info
    :type admin_info: dict | bytes

    """
    admin_info = ServicesContractAdminUpdateDto.from_dict(admin_info)
    return web.Response(status=200)
