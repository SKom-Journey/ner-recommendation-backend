from utils.response import response
from services.admins import admin_by_username
from bcrypt import checkpw

def login_admin_controller(json: dict):
    adminByUsername = admin_by_username(json['username'])
    if adminByUsername == None:
        return response("Username Not Found", "ERROR", True)
    
    if checkpw(json['password'].encode(), adminByUsername['password'].encode()):
        return response(adminByUsername)
    else:
        return response("Password Incorrect", "ERROR", True)