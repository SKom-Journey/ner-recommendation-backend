from utils.response import response
from services.qrs import qrs

def get_qrs_controller():
    return response(qrs())