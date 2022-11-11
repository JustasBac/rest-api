import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id], 404
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}, 404
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="'price' and 'name' should be included in the payload")

        try:
            item = items[item_id]

            # item["price"] = item_data["price"]
            # item["name"] = item_data["name"]
            item |= item_data
            return item, 201
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/items")
class Item(MethodView):
    def get(self):
        return {"items": list(items.values())}


@blp.route("/item")
class Item(MethodView):
    @blp.arguments(ItemSchema)
    def post(self, item_data):  # item_data coming from ItemSchema
        item_data = request.get_json()

        for item in items.values():
            if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
                abort(400, message="Such item already exists")

        # if item_data["store_id"] not in stores:
        #     print("not found")
        #     abort(404, message="Store not found")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
