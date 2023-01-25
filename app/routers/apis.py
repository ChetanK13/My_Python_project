from fastapi import APIRouter, status, HTTPException, Depends
from models.apis_model import PostSchema,  UserSchema, UserLoginSchema, UpdateUser, UpdateSchema, MessageSchema
from DB_connection.db import collection, collection2, collection3, result
from Schemas.schema import serializeDict, serializeList
from auth.utils import get_hashed_password, verify_password
from validation.handler import validate_password, merge, validate_mobile
from fastapi.encoders import jsonable_encoder
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from bson import ObjectId
import pika
user = APIRouter()


# -------------------------USER--------------------------------------------


@user.post('/signup', tags=["user"])
async def create_user(user: UserSchema):
    validate_password(user.password)
    validate_mobile(user.mobile_no)
    a = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'gender': user.gender,
        'mobile_no': user.mobile_no,
        'email': user.email,
        'emp_id': user.emp_id,
        'password': get_hashed_password(user.password)
    }
    collection.insert_one(a)
    return signJWT(user.email)


@user.get('/allusers', tags=["user"])
async def find_all_users():
    return serializeList(collection.find({}, {"password": 0}))

# , dependencies=[Depends(JWTBearer())]


@user.get("/data1/{id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_entity(id: str):
    a = serializeDict(collection.find_one(
        {"_id": ObjectId(id)}, {"password": 0}))
    return a

# , dependencies=[Depends(JWTBearer())]


@user.put('/{id}', dependencies=[Depends(JWTBearer())], tags=["user"])
async def update_user(id, user: UpdateUser):
    if user.mobile_no:
        validate_mobile(user.mobile_no)
    a = serializeDict(collection.find_one(
        {"_id": ObjectId(id)}, {"password": 0}))
    stored_item_model = UpdateUser(**a)
    update_data = user.dict(exclude_unset=True)
    updated_data = stored_item_model.copy(update=update_data)
    collection.find_one_and_update({"_id": ObjectId(id)}, {
                                   "$set": dict(updated_data)})
    return serializeDict(collection.find_one({"_id": ObjectId(id)}, {"password": 0}))


@user.delete('/{id}', tags=["user"])
async def delete_user(id):
    serializeDict(collection.find_one_and_delete({"_id": ObjectId(id)}))
    return "DELETED"


# @user.delete('/data/{first_name}', tags=["user"])
# async def delete_user(first_name:str):
#     serializeDict(collection.find_one_and_delete({"first_name":first_name}))
#     return "DELETED"


@user.post('/login', tags=["user"])
async def login(data: UserLoginSchema):
    try:
        a = serializeDict(collection.find_one({"email": data.email}, None))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    hashed_pass = a['password']
    if not verify_password(data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return signJWT(data.email)


# --------------------------emp details--------------------------------------


@user.post('/data', tags=["emp_details"])
async def create_user(data: PostSchema):
    collection2.insert_one(dict(data))
    return "created"


@user.get('/data', tags=["emp_details"])
async def find_all_users():
    return serializeList(collection2.find())
    # print(serializeList(collection2.find()))


@user.get("/data/{emp_id}", tags=["emp_details"])
async def get_entity(emp_id: str):
    return serializeDict(collection2.find_one({"emp_id": emp_id}))


@user.put('/data/{emp_id}', tags=["emp_details"])
async def update_user(emp_id: str, user: UpdateSchema):
    a = serializeDict(collection2.find_one({"emp_id": emp_id}))
    stored_item_model = UpdateSchema(**a)
    update_data = user.dict(exclude_unset=True)
    updated_data = stored_item_model.copy(update=update_data)
    collection2.find_one_and_update(
        {"emp_id": emp_id}, {"$set": dict(updated_data)})
    return serializeDict(collection2.find_one({"emp_id": emp_id}))


@user.delete('/data/{emp_id}', tags=["emp_details"])
async def delete_user(emp_id: str):
    return serializeDict(collection2.find_one_and_delete({"emp_id": emp_id}))


# -------------------------------------combined details----------------------------------------------------


@user.get("/emp_details/{emp_id}", tags=["emp_details"])
async def get_entity(emp_id: str):
    a = serializeDict(collection.find_one({"emp_id": emp_id}, {"password": 0}))
    b = serializeDict(collection2.find_one({"emp_id": emp_id}))
    merge(a, b)
    return a


# - - - - - - - - - - - - - - - - - - - - -Message - - - - - - - - - - - - - - - - - - - - - - - -


@user.post("/msg/", tags=["Message"])
async def massage(data: MessageSchema):
    d = data.dict()
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel1 = connection.channel()
    sender = d['SENDER']
    receiver = d['RECEIVER']
    entity = d['MESSAGE']
    channel1.queue_declare(queue=sender)
    channel1.basic_publish(exchange='', routing_key=sender, body=entity)
    channel1.queue_declare(queue=receiver)

    def callback(ch, method, properties, body):
        print("Message======> %r " % body.decode())
        connection.close()
        collection3.insert_one(
            {"SENDER": sender, "RECEIVER": receiver, "MESSAGE": body.decode()})
    channel1.basic_consume(
        queue=sender, on_message_callback=callback, auto_ack=True)
    channel1.start_consuming()
    return {"status": "OK"}


@user.delete('/msgdlt/{SENDER}', tags=["Message"])
async def delete_user(SENDER: str):
    return serializeDict(collection3.find_one_and_delete({"SENDER": SENDER}))

# ------------------------------------------------------------------------------------------
# @user.get('/alldataaaaaaa', tags=["data"])
# async def find_all_users():
#     for a in result:
#         b = str(a)
#         return b
