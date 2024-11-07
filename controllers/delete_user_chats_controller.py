from utils.response import response
from services.chats import delete_chats_by_user_id

def delete_user_chats_controller(user_id: str):
    return response(delete_chats_by_user_id(user_id))