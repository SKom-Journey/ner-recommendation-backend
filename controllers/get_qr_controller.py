from utils.response import response
from services.qrs import qr

def get_qr_controller(table_number: str):
    return response(qr(table_number))