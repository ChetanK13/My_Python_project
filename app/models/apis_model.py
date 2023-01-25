from pydantic import BaseModel, EmailStr
from typing import Optional

class UpdateSchema(BaseModel):
    designation: Optional[str] 
    salary: Optional[str]

class PostSchema(UpdateSchema):
    emp_id: str
    designation: str 
    salary: str

# --------------------------------------------

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    mobile_no: Optional[str]
    email: Optional[EmailStr] 
    
class UserSchema(UpdateUser):
    first_name: str 
    last_name: str
    gender: str
    mobile_no: str
    email: EmailStr
    emp_id: str
    password: str  
    
# ----------------------------------------------

class UserLoginSchema(BaseModel):
    email: EmailStr 
    password: str

# -----------------------------------------------

class MessageSchema(BaseModel):
    SENDER: str
    RECEIVER: str
    MESSAGE: str
    