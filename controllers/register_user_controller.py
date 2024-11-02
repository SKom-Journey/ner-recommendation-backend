from utils.response import response
from services.users import create_user, user_by_email

def register_user_controller(json: dict):
    checkEmailExist = user_by_email(json['email'])
    if checkEmailExist == None:
        return response(create_user(
            json['email'],
            json['password'],
            json['email'],
            False
        ))
    
    return response("Email Already Exist", "ERROR", True)