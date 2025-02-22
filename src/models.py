import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    likes_id = Column(Integer, ForeignKey('post.id'))
    likes = relationship(Likes)

class Comments(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comments_id = Column(Integer, ForeignKey('post.id'))
    comments = relationship(Comments)

    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


