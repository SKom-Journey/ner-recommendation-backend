from utils.response import response
from services.qrs import create_qr, qr

def create_qr_controller(json: dict):
    checkIfExist = qr(json['table_number'])

    if checkIfExist != None:
        return response("Table Number Already Exist", "ERROR", True)

    return response(create_qr(
        json['table_number']
    ))