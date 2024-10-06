from utils.response import response
from utils.ner_module import get_recommendation

def get_menu_recommendation_controller():
    recommendation = get_recommendation()
    return response(recommendation)