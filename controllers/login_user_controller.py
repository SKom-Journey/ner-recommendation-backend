from utils.response import response
from services.users import user_by_email
from bcrypt import checkpw

def login_user_controller(json: dict):
    userByEmail = user_by_email(json['email'])
    if userByEmail == None:
        return response("Email Not Found", "ERROR", True)
    
    if checkpw(json['password'].encode(), userByEmail['password'].encode()):
        return response(userByEmail)
    else:
        return response("Password Incorrect", "ERROR", True)