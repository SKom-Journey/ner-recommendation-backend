from utils.response import response
from services.users import create_user, user_by_email
import bcrypt

def login_user_controller(json: dict):
    userByEmail = user_by_email(json['email'])
    if userByEmail == None:
        return response("Email Not Found", "ERROR", True)
    
    if bcrypt.checkpw(json['password'].encode(), userByEmail['password'].encode()):
        return response(userByEmail)
    else:
        return response("Password Incorrect", "ERROR", True)