from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest
from bson import ObjectId
from bson.objectid import InvalidId
from umongo import ValidationError
from . import services, schemas


routes = web.RouteTableDef()


def validate_object_id(object_id: str) -> ObjectId:
    try:
        object_id = ObjectId(object_id)
    except InvalidId:
        raise HTTPBadRequest(reason='Invalid id.')
    return object_id


@routes.post('/items')
async def create_item(request: web.Request) -> web.Response:
    try:
        schema = schemas.ItemSchema(strict=True)
        data = schema.load(await request.json()).data
    except ValidationError as error:
        raise HTTPBadRequest(reason=error.messages)

    item = await services.create_item(data)
    return web.json_response(item.dump(), status=201)


@routes.post('/items/find-by-id')
async def find_by_id(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except ValidationError as error:
        raise HTTPBadRequest(reason=error.messages)

    item_id = validate_object_id(data['id'])
    item = await services.find_item(item_id)

    return web.json_response(item.dump(), status=200)


@routes.post('/items/filter')
async def find_by_filter(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except ValidationError as error:
        raise HTTPBadRequest(reason=error.messages)

    items = await services.find_items(data)
    return web.json_response([item.name async for item in items], status=200)
