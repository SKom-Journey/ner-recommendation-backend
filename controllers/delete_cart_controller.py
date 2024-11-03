from utils.response import response
from services.carts import delete_cart

def delete_cart_controller(json: dict):
    return response(delete_cart(json['user_id'], json['menu_id'], json.get('note', "")))