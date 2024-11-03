from utils.mongodb import db
from models.Order import Order
from bson import ObjectId
from datetime import datetime
from services.menus import menu_by_id
from services.users import user_by_id

tb_name = 'orders'

def create_order(items, table_number: int, user_id: str):
    menu_items = []

    for item in items:
        get_menu = menu_by_id(item['id'])
        if get_menu:
            menu_items.append({
                **item,
                "name": get_menu['title'],
                "price": get_menu['price'] * item['total']
            })

    order_id = db.get_collection(tb_name).insert_one({"user_id": ObjectId(user_id), "items": menu_items, "is_finished": False, "table_number": table_number, "created_at": datetime.now()}).inserted_id
    order = db.get_collection(tb_name).find_one({"_id": ObjectId(order_id)})
    user = user_by_id(user_id)
    return Order(
        table_number = str(order['table_number']),
        items = order['items'],
        user_id = str(order['user_id']),
        user_name = str(user['name']),
        is_finished = bool(order['is_finished']),
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