from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from blog import models,schemas
 
# Here We defined all function which is used in blog routes

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(request:schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title,body=request.body, creator_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


def get_particularBlog(id:int,db:Session):
    particular_blog = db.query(models.Blog).filter(models.Blog.id  == id).first()
    if not particular_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
    return particular_blog


def destroy_blog(id:int,db:Session):
    delete_particular_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not delete_particular_blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"blog with the id {id} is not exist.")
    delete_particular_blog.delete(synchronize_session=False)
    db.commit()    
    return {'status':'delete successfully'}


def update_blog(id:int,request:schemas.Blog, db:Session):
    update_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not update_blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"blog with the id {id} is not exist.")
    update_blog.update(request.dict())
    db.commit()
    return 'updated'