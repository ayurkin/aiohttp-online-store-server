from marshmallow import Schema
from .models import Item


ItemSchema: Schema = Item.schema.as_marshmallow_schema()
