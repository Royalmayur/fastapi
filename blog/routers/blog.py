from fastapi import APIRouter,status,Depends
from blog import schemas,database,Oauth2
from sqlalchemy.orm.session import Session
from typing import List
from blog.repository import blog


router = APIRouter(
    prefix = '/blog',
    tags=["Blogs"],
)

get_db = database.get_db #  Get Database with dependency

#here slash means base Url .basically defined "path" or route or endpoint .Using path operation decorater
@router.get('/',response_model=List[schemas.ShowBlog])
def show_blogs(db:Session=Depends(get_db),current_user:schemas.User = Depends(Oauth2.get_current_user)):
    return blog.get_all(db)



@router.post('/',status_code=status.HTTP_201_CREATED) # Post operation is for create something
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User = Depends(Oauth2.get_current_user)):
    return blog.create_blog(request,db)


@router.get('/{id}',status_code =status.HTTP_200_OK,response_model=schemas.ShowBlog)  #we can defined dynamically routing by curly braces
def show_particularBlog(id:int, db:Session=Depends(get_db)): #here we defined type converstion also
    return blog.get_particularBlog(id,db)


@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(get_db),current_user:schemas.User = Depends(Oauth2.get_current_user)):
    return blog.destroy_blog(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blogs(id:int,request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User = Depends(Oauth2.get_current_user)):
    return blog.update_blog(id,request,db)