from utils.response import response
from services.orders import create_order
from models.Order import Order

def create_order_controller(json: dict):
    return response(create_order(json['items'], json['table_number']))