from marshmallow import Schema, fields


class ItemSchema(Schema):
    # id is not being validated, just returned to a user, thats why dump_only
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    # id is not being validated, just returned to a user, thats why dump_only
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
