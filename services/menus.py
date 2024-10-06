from utils.mongodb import db
from models.Menu import Menu

tb_name = 'menus'

def menus():
    result = []
    for menu in db.get_collection(tb_name).find():
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