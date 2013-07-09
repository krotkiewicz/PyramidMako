from sqlalchemy import (
    Column,
    Integer,
    Text,
    Float)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class HistoryModel(Base):
    __tablename__ = 'first_model'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text)
    price_allegro = Column(Float)
    url_allegro = Column(Text)
    price_nokaut = Column(Float)
    url_nokaut = Column(Text)

    def __init__(self, name, price_allegro, url_allegro, price_nokaut, url_nokaut):
        self.name = name
        self.price_allegro = price_allegro
        self.url_allegro = url_allegro
        self.price_nokaut = price_nokaut
        self.url_nokaut = url_nokaut

    def __repr__(self):
        return "<User('%s', '%.2f' ,'%s','%.2f','%s')>" % (
            self.name,
            self.price_allegro,
            self.url_allegro,
            self.price_nokaut,
            self.url_nokaut
        )


class User(Base):
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    name = Column(Text)
    password = Column(Text)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.password)
