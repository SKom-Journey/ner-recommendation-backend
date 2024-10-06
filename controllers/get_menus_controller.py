from utils.response import response
from services.menus import menus
from models.Menu import Menu

def get_menus_controller():
    data = menus()
    result = []
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
    return response(result)