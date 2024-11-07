from utils.mongodb import db
from bson import ObjectId
from models.Chat import Chat
from datetime import datetime
from pymongo import DESCENDING, ASCENDING
from services.menus import menus_by_ids

tb_name = 'chats'

def chats_by_user_id(user_id: str, limit: int = 5, sort_date: int = 1):
    result = []
    sort_order = ASCENDING if sort_date == 1 else DESCENDING
    chats = db.get_collection(tb_name).find({"user_id": user_id}).sort("created_at", sort_order).limit(limit)

    for chat in chats:
        chat_ids = []
        menus = []
        
        for chat_id in chat["items"]:
            chat_ids.append(chat_id)
        
        for menu in menus_by_ids(chat_ids):
            menus.append(menu)
        
        result.append(Chat(
            id = str(chat["_id"]),
            user_id = str(chat["user_id"]),
            user_message = str(chat["user_message"]),
            items = chat['items'],
            menus = menus,
            created_at = chat["created_at"].isoformat()
        ).model_dump())

    return result

def create_chat(user_id: str, user_message: str, items: list[str]):
    chat_id = db.get_collection(tb_name).insert_one({
        "user_id": user_id, 
        "user_message": user_message,
        "items": items,
        "created_at": datetime.now()
    }).inserted_id

    chat = db.get_collection(tb_name).find_one({"_id": ObjectId(chat_id)})
    
    return Chat(
        id = str(chat["_id"]),
        user_id = str(chat["user_id"]),
        user_message = str(chat["user_message"]),
        items = chat["items"],
        created_at = chat["created_at"].isoformat()
    ).model_dump() 
 
def delete_chats_by_user_id(user_id: str):
    deleted_count = db.get_collection(tb_name).delete_many({
        "user_id": user_id
    }).deleted_count
    
    return deleted_count
 