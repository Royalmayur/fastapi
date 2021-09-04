from blog.database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Here we create our sqlalchemy models Which is converted into tables in our database Because of ORM library

class Blog(Base):
    __tablename__='blogs'

    id = Column(Integer,primary_key=True,index=True)
    title= Column(String)
    body = Column(String)
    creator_id = Column(Integer, ForeignKey("Users.id"))
    creator = relationship('User', back_populates='blogs') # Setup for map tables


class User(Base):
    __tablename__ = 'Users' 

    id = Column(Integer,primary_key = True,index = True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    blogs = relationship('Blog', back_populates='creator')
