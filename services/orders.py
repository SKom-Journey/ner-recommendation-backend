from utils.mongodb import db
from models.Order import Order
from bson import ObjectId
from datetime import datetime
from services.menus import menu

tb_name = 'orders'

def create_order(items, table_number: int):
    menu_items = []

    for item in items:
        get_menu = menu(item['id'])
        if get_menu:
            menu_items.append({
                **item,
                "price": int(get_menu['price']) * int(item['total'])
            })

    order_id = db.get_collection(tb_name).insert_one({"items": menu_items, "table_number": table_number, "created_at": datetime.now()}).inserted_id
    order = db.get_collection(tb_name).find_one({"_id": ObjectId(order_id)})
    return Order(
        table_number = str(order['table_number']),
        items = order['items'],
        id = str(order['_id']),
        created_at = order['created_at'].isoformat(),
    ).model_dump()

def orders():
    result = []
    for order in db.get_collection(tb_name).find().sort("created_at", 1):
        result.append(
            Order(
                table_number = str(order['table_number']),
                items = order['items'],
                id = str(order['_id']),
                created_at = order['created_at'].isoformat(),
            )
            .model_dump()
        )
    return result