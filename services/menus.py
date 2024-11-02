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
    for menu in db.get_collection(tb_name).find(entities).limit(5):
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

def menus_by_ids(ids: list[str]):
    result = []
    filter_ids = []

    for menu_id in ids:
        filter_ids.append(ObjectId(menu_id))

    for menu in db.get_collection(tb_name).find({"_id": {"$in": filter_ids}}):
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

def menus_by_not_in_ids(ids: list[str]):
    result = []
    filter_ids = []

    for menu_id in ids:
        filter_ids.append(ObjectId(menu_id))

    for menu in db.get_collection(tb_name).find({"_id": {"$nin": filter_ids}}):
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