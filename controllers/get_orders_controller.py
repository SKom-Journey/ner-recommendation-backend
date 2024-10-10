from utils.response import response
from services.orders import orders

def get_orders_controller():
    return response(orders())