from utils.response import response
from services.categories import delete_category
from models.Order import Order

def delete_category_controller(id):
    return response(delete_category(id))