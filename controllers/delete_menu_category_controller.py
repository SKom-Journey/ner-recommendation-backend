from utils.response import response
from services.menu_categories import delete_menu_category

def delete_menu_category_controller(json: dict):
    return response(delete_menu_category(json['category_id'], json['menu_id']))