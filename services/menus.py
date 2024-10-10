from utils.mongodb import db
from models.Menu import Menu
from bson import ObjectId

tb_name = 'menus'

def menus(keyword: str):
    result = []
    data =  db.get_collection(tb_name).find({
        "$or": [
            {
                "title": {
                    "$regex": keyword, 
                    "$options": "i"
                }
            },
            {
                "description": {
                    "$regex": keyword, 
                    "$options": "i"
                }
            }
        ]
    })
    for menu in data:
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=menu['price'],
                img=menu['img']
            )
            .model_dump()
        )
    return result

def find_by_entities(entities: dict):
    result = []
    for menu in db.get_collection(tb_name).find(entities):
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=menu['price'],
                img=menu['img']
            )
            .model_dump()
        )
    return result

def menu(id: str):
    data = db.get_collection(tb_name).find_one({"_id": ObjectId(id)})
    return Menu(
        id=str(data['_id']),
        title=data['title'],
        description=data['description'],
        price=data['price'],
        img=data['img']
    ).model_dump()