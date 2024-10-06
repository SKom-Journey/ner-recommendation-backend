from utils.mongodb import db

db_name = 'menus'

def menus():
    return db.get_collection(db_name).find()