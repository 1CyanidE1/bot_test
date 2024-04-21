from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, BigInteger
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

from bot.config import config


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    lang = Column(String)


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    link = Column(String)
    username = Column(String, ForeignKey('users.username'))
    file_name = Column(String)

    user = relationship('User')


engine = create_engine(config.postgres.link)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
