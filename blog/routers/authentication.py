from fastapi import APIRouter,HTTPException,status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from blog  import database,models,JWTtokens
from sqlalchemy.orm.session import Session
from blog.hashing import Hash


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.user_email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"{request.username} is not exist!!")
    if not Hash.verify(user.user_password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Invalid Password")

    # generate JWT token and return

    access_token = JWTtokens.create_access_token(data={"sub": user.user_email})
    return {"access_token": access_token, "token_type": "bearer"}