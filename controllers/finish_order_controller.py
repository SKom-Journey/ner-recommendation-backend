from utils.response import response
from services.orders import finish_order

def finish_order_controller(id: str):
    return response(finish_order(id))