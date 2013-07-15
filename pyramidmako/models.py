import datetime
from sqlalchemy import Column, Integer, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class History(Base):
    __tablename__ = 'history'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    user_id_ = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    count = Column(Integer, default=1)

    status_allegro = Column(Text)
    price_allegro = Column(Float)
    url_allegro = Column(Text)

    status_nokaut = Column(Text)
    price_nokaut = Column(Float)
    url_nokaut = Column(Text)


class User(Base):
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
