from utils.response import response
from services.orders import create_order

def create_order_controller(json: dict):
    return response(create_order(json['items'], json['table_number'], json['user_id']))