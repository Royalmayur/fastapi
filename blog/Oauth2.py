from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from blog import JWTtokens


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    "This method is for cheak current user is authorized or not!!"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWTtokens.verify_token(token,credentials_exception)