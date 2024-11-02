from utils.response import response
from services.menu_categories import create_menu_category, get_menu_category

def create_menu_category_controller(json: dict):
    checkCategoryExist = get_menu_category(json['category_id'], json['menu_id'])
    if checkCategoryExist == None:
        return response(create_menu_category(json['category_id'], json['menu_id']))
    return response("Menu Already Inside This Category", "ERROR", True)