from umongo import Document, fields
from .db import instance


@instance.register
class Item(Document):
    name = fields.StringField(required=True)
    description = fields.StrField()
    parameters = fields.DictField()
