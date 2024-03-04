import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(1250))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    reaction_id = Column(Integer, ForeignKey('reaction.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(1250))
    commenter_id = Column(Integer, ForeignKey('follower.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Reaction(Base):
    __tablename__ = 'reaction'
    id = Column(Integer, primary_key=True)
    reaction_type = Column(String(250))
    reacter_id = Column(Integer, ForeignKey('follower.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    following_id = Column(Integer, ForeignKey('user.id'))
    following = relationship(User)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)
    reacter_id = Column(Integer, ForeignKey('reaction.id'))
    reacter = relationship(Reaction)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
