import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    mail = Column(String(50), nullable=False)
    password = Column(String(50), nullable= False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    photo = Column(String(250))
    created = Column(String(250), nullable=False)
    update= Column(DATETIME,nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))


class Like(Base):
    __tablename__= 'like'
    id= Column(Integer, primary_key=True)
    post_id = Column(Integer , ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))   
    quantity= Column(Integer, nullable=True)

class Followers(Base):
    __tablename__= 'followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ('user.id'))
    follow_id = Column(Integer , ForeignKey('user.id')) 
        
class Comment(Base):   
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer , ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id')) 
    comment = Column(String(250), nullable=False)
    created = Column(DATETIME, nullable=False)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
##try:
##    result = render_er(Base, 'diagram.png')
##    print("Success! Check the diagram.png file")
##except Exception as e:
##    print("There was a problem genering the diagram")
##    raise e"""
