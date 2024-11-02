from utils.mongodb import db
from models.MenuCategory import MenuCategory
from bson import ObjectId
from datetime import datetime

tb_name = 'menu_categories'

def create_menu_category(category_id: str, menu_id: str):
    menu_category_id = db.get_collection(tb_name).insert_one({"category_id": ObjectId(category_id), "menu_id": ObjectId(menu_id), "created_at": datetime.now()}).inserted_id
    menu_category = db.get_collection(tb_name).find_one({"_id": ObjectId(menu_category_id)})
    return MenuCategory(
        menu_id = str(menu_category['menu_id']),
        category_id = str(menu_category['category_id']),
        id = str(menu_category['_id']),
        created_at = menu_category['created_at'].isoformat(),
    ).model_dump()

def delete_menu_category(category_id: str, menu_id: str):
    delete = db.get_collection(tb_name).delete_one({"category_id": ObjectId(category_id), "menu_id": ObjectId(menu_id)})
    return delete.deleted_count

def get_menu_category(category_id: str, menu_id: str):
    menu_category = db.get_collection(tb_name).find_one({"category_id": ObjectId(category_id), "menu_id": ObjectId(menu_id)})
    if menu_category == None:
        return None
    return MenuCategory(
        menu_id = str(menu_category['menu_id']),
        category_id = str(menu_category['category_id']),
        id = str(menu_category['_id']),
        created_at = menu_category['created_at'].isoformat(),
    ).model_dump()