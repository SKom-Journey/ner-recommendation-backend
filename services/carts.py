from utils.mongodb import db
from models.Cart import Cart
from bson import ObjectId
from datetime import datetime
from services.menus import menu_by_id

tb_name = 'carts'

def create_cart(user_id: str, menu_id: str, note: str | None):
    checkCartExist = get_cart_by_user_id_and_menu_id(user_id, menu_id)
    
    data = {}

    if note != None:
        data['note'] = note

    if checkCartExist:
        db.get_collection(tb_name).update_one(
            {
                "_id": ObjectId(checkCartExist['id'])
            },
            {
                "$set": data,
                "$inc": {"quantity": 1}
            }
        )
        return get_cart(checkCartExist['id'])

    cart_id = db.get_collection(tb_name).insert_one({"quantity": 1, "user_id": ObjectId(user_id), "menu_id": ObjectId(menu_id), "note": note, "created_at": datetime.now()}).inserted_id
    return get_cart(cart_id)

def delete_cart(user_id: str, menu_id: str, note: str):
    checkCartExist = get_cart_by_user_id_and_menu_id(user_id, menu_id)

    if checkCartExist:
        if checkCartExist['quantity'] > 1:
            db.get_collection(tb_name).update_one(
                {
                    "_id": ObjectId(checkCartExist['id'])
                },
                {
                    "$set": {"note": note},
                    "$inc": {"quantity": -1}
                }
            )
            return get_cart(checkCartExist['id'])
        else:
            db.get_collection(tb_name).delete_one({"user_id": ObjectId(user_id), "menu_id": ObjectId(menu_id)})
    return None

def get_carts_by_user_id(user_id: str):
    result = []
    for cart in db.get_collection(tb_name).find({"user_id": ObjectId(user_id)}):
        menu = menu_by_id(cart['menu_id'])
        result.append(
            Cart(
                quantity = int(cart['quantity']),
                menu_id = str(cart['menu_id']),
                user_id = str(cart['user_id']),
                note = str(cart['note']),
                id = str(cart['_id']),
                created_at = cart['created_at'].isoformat(),

                menu = menu
            ).model_dump()
    )
    return result

def get_cart_by_user_id_and_menu_id(user_id: str, menu_id: str):
    cart = db.get_collection(tb_name).find_one({"user_id": ObjectId(user_id), "menu_id": ObjectId(menu_id)})

    if cart == None:
        return None
    
    return Cart(
        quantity = int(cart['quantity']),
        menu_id = str(cart['menu_id']),
        user_id = str(cart['user_id']),
        note = str(cart['_id']),
        id = str(cart['_id']),
        created_at = cart['created_at'].isoformat(),
    ).model_dump()

def get_cart(id: str):
    cart = db.get_collection(tb_name).find_one({"_id": ObjectId(id)})

    if cart == None:
        return None
    
    return Cart(
        quantity = int(cart['quantity']),
        menu_id = str(cart['menu_id']),
        user_id = str(cart['user_id']),
        note = str(cart['note']),
        id = str(cart['_id']),
        created_at = cart['created_at'].isoformat(),
    ).model_dump()

def update_note_by_id(id: str, note: str):
    db.get_collection(tb_name).update_one(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": {
                "note": note
            }
        }
    )
    return get_cart(id)

def delete_cart_by_user_id_and_menu_id(user_id: str, menu_id: str):
    delete = db.get_collection(tb_name).delete_one(
        {
            "user_id": ObjectId(user_id),
            "menu_id": ObjectId(menu_id)
        }
    )
    return delete.deleted_count