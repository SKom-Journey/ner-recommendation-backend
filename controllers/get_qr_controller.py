from utils.response import response
from services.qrs import qr

def get_qr_controller(id: str):
    return response(qr(id))