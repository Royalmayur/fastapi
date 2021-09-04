from typing import List,Optional
from pydantic import BaseModel


#  Here we create our pydantic schemas(models) . These schemas defined our response and request body 

class Blogbranch(BaseModel):  #Extend from BaseModel class from pydantic schemas
    title : str
    body :str  

class Blog(Blogbranch):
    # Pydantic models can be created from arbitrary class instances to support models that map to ORM objects.
    class Config():
        orm_mode = True



class User(BaseModel):
    user_name :str
    user_email: str
    user_password : str

# These shows schemas is for defined custom response
class User_show(BaseModel):
    user_name : str
    user_email : str
    blogs:List[Blog]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title : str
    body : str
    creator : User_show

    class Config():
        orm_mode = True


class Login(BaseModel):
    password : str
    username : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None