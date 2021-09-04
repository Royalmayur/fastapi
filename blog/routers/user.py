from fastapi import APIRouter,status,Depends
from blog import schemas,database
from sqlalchemy.orm.session import Session
from blog.repository import user



# If you are building an application or a web API
# FastAPI provides a convenience tool to structure your application while keeping all the flexibility.
"""
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
"""

# That's why we should use external routers directory which is defined every routes file.
# for defining Routes, we use APIRouter class for create routes

router = APIRouter(
    prefix = '/user', # defined routes Url
    tags=["Users"]   # Tags are used for catagorized our routes.
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.User_show)  # "?limit=10&published=true" "?" is query in url but don't need to specify here
def create_user(request:schemas.User, db:Session=Depends(get_db)): #here we handle query paramenters ,i proovide default value also
    return user.create(request,db)

# Fast api is smart enough to identify which is query parameter and path parameter ,if path have any params then api check same name params have in  path operation function then it make path params otherwise make it query.

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.User_show) #route defined ,And its called operation on the path and get is operation
#Called, Path operation function
def get_user(id:int, db:Session=Depends(get_db)):
    return user.getUser(id,db)