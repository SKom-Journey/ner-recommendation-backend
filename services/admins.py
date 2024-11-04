from utils.mongodb import db
from models.Admin import Admin

tb_name = 'admins'

def admin_by_username(username: str):
    admin = db.get_collection(tb_name).find_one({"username": username})
    if admin != None:
        return Admin(
            id=str(admin['_id']),
            password=admin['password'],
            username=admin['username'],
            created_at=admin['created_at'].isoformat(),
        ).model_dump() 
    
    return None