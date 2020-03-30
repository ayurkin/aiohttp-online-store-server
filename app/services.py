from typing import AsyncIterable, Dict
from aiohttp.web_exceptions import HTTPNotFound
from bson import ObjectId
from .models import Item


async def find_items(data) -> AsyncIterable[Item]:
    query_dict = {"$and": []}

    if len(data) == 0:
        return Item.find({})

    for field in data:
        if field == "name":
            query_dict["$and"].append({field: data[field]})
        else:
            query_dict["$and"].append({f"parameters.{field}": data[field]})
    return Item.find(query_dict)


async def create_item(data: Dict) -> Item:
    item = Item(**data)
    await item.commit()
    return item


async def find_item(item_id: ObjectId) -> Item:
    item = await Item.find_one({'_id': item_id})
    if not item:
        raise HTTPNotFound()

    return item
