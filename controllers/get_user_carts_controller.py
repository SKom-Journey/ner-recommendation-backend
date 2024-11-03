from utils.response import response
from services.carts import get_carts_by_user_id

def get_user_carts_controller(user_id: str):
    return response(get_carts_by_user_id(user_id))