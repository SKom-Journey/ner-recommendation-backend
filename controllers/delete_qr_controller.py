from utils.response import response
from services.qrs import delete_qr

def delete_qr_controller(id: str):
    return response(delete_qr(id))