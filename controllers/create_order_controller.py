from utils.response import response
from services.orders import create_order
from services.carts import delete_cart_by_user_id_and_menu_id

def create_order_controller(json: dict):
    order = create_order(json['items'], json['table_number'], json['user_id'])
    for item in order['items']:
        delete_cart_by_user_id_and_menu_id(order['user_id'], item['id'])
    return response(order)