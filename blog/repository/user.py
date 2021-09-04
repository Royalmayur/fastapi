from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from blog import schemas,models
from blog.hashing import Hash

# Here We defined all function which is used in User routes

def create(request:schemas.User, db:Session):
    newUser = models.User(user_name = request.user_name, user_email = request.user_email, user_password = Hash.bcrypt(request.user_password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def getUser(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with the id {id} is not exist.")

    return user