from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)











# @user.post('/')
# async def login(data: UserLoginSchema):
#     a = serializeDict(collection.find_one({"email":data.email}, None))
#     if a is None: 
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )
#     hashed_pass = a['password']
#     if not verify_password(data.password, hashed_pass):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )
#     return signJWT(data.email)
