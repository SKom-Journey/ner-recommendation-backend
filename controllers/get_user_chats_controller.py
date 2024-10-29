from utils.response import response
from services.chats import chats_by_user_id

def get_user_chats_controller(user_id: str):
    return response(chats_by_user_id(user_id))