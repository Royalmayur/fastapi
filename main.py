from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog,user,authentication

# Intialize our fastapi
app = FastAPI()

# Here we create tables in our database, It's like "Migration"
models.Base.metadata.create_all(engine)

# Here we include all my external routes from routers directory
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)















# @app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create(request:schemas.Blog,db:Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body, creator_id =1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',response_model=List[schemas.ShowBlog], tags=['Blogs'])
# def show_blogs(db:Session=Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code =status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['Blogs'])
# def show_particularBlog(id:int,response: Response, db:Session=Depends(get_db)):
#     particular_blog = db.query(models.Blog).filter(models.Blog.id  == id).first()
#     if not particular_blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Blog with the id {id} is not available')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with the id {id} is not available'}
#     return particular_blog


# @app.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def delete_blog(id:int,db:Session=Depends(get_db)):
#     delete_particular_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not delete_particular_blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"blog with the id {id} is not exist.")
#     delete_particular_blog.delete(synchronize_session=False)
#     db.commit()    
#     return {'status':'delete successfully'}


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
# def update_blogs(id:int,request:schemas.Blog, db:Session=Depends(get_db)):
#     update_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not update_blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"blog with the id {id} is not exist.")
#     update_blog.update(request.dict())
#     db.commit()
#     return 'updated'




# @app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.User_show,tags=['User'])
# def create_user(request:schemas.User, db:Session=Depends(get_db)):
#     newUser = models.User(user_name = request.user_name, user_email = request.user_email, user_password = Hash.bcrypt(request.user_password))
#     db.add(newUser)
#     db.commit()
#     db.refresh(newUser)
#     return newUser


# @app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.User_show,tags=['User'])
# def get_user(id:int, db:Session=Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with the id {id} is not exist.")

#     return user