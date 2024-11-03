from utils.response import response
from services.carts import update_note_by_id

def update_cart_note_by_id_controller(id: str, json: dict):
    return response(update_note_by_id(id, json['note']))