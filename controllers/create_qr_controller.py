from utils.response import response
from services.qrs import create_qr
from models.QR import QR

def create_qr_controller(json: dict):
    return response(create_qr(
        json['table_number'],
        json['is_enabled']
    ))