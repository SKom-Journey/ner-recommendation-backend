from utils.mongodb import db
from bson import ObjectId
from models.QR import QR

tb_name = 'qrs'

def delete_qr(id: str):
    delete = db.get_collection(tb_name).delete_one({"_id": ObjectId(id)})
    return delete.deleted_count 

def create_qr(table_number: str):
    qr_id = db.get_collection(tb_name).insert_one({"table_number": table_number}).inserted_id
    qr = db.get_collection(tb_name).find_one({"_id": ObjectId(qr_id)})
    return QR(
        id=str(qr['_id']),
        table_number=qr['table_number'],
    ).model_dump() 
 
def qr(table_number: str):
    qr = db.get_collection(tb_name).find_one({"table_number": table_number})
    if qr == None:
        return None
    return QR(
        id=str(qr['_id']),
        table_number=qr['table_number'],
    ).model_dump() 

def qrs():
    result = []
    for qr in db.get_collection(tb_name).find():
        result.append(
            QR(
                id=str(qr['_id']),
                table_number=qr['table_number'],
            )
            .model_dump()
        )
    return result