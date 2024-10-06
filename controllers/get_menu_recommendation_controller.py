from utils.response import response
from utils.ner_module import get_entities
from services.menus import find_by_entities

def get_menu_recommendation_controller(text: str):
    entities = get_entities(text)

    query = {}

    for key, values in entities.items():
        if values:
            query[key] = {"$in": values}
    
    return response(find_by_entities(query))