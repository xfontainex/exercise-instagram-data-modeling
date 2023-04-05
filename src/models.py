import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

    
class User(Base) :
    __tablename__="User"
    id=Column(Integer, primary_key=True) 
    username = Column(String (256))  
    firstname = Column(String (256))  
    lastname = Column(String (256))  
    email = Column(String (256)) 
    post = relationship("Post")
    comment = relationship("Comment", backref='User', lazy=True)
    post = relationship('Post', backref='User', lazy=True)
    
class Post(Base) :
    __tablename__="Post"
    id=Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))

class Followers(Base): 
    __tablename__ = "Followers"
    id=Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("User.id"))
    user_to_id = Column(Integer, ForeignKey("User.id"))

class Media(Base) :
    __tablename__="Media"
    id=Column(Integer, primary_key=True)
    mediatype= Column(String(256))
    url = Column(String(256))
    post_id = Column(Integer, ForeignKey("Post.id"))
    
class Comment(Base) :
    __tablename__="Comment"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("User.id"))
    post_id = Column(Integer, ForeignKey("User.id"))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
