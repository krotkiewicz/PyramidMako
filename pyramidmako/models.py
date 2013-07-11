import datetime
from sqlalchemy import Column, Integer, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class HistoryModel(Base):
    __tablename__ = 'first_model'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    price_allegro = Column(Float)
    url_allegro = Column(Text)
    price_nokaut = Column(Float)
    url_nokaut = Column(Text)
    user_id_ = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status_allegro = Column(Text, default='')
    status_nokaut = Column(Text, default='')
    comparison_allegro = Column(Text, default='price')
    comparison_nokaut = Column(Text, default='price')


class User(Base):
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
