# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from app_demo.database import Base


metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    name = Column(String(100), unique=True, server_default=text("''::character varying"))
    address = Column(String(100), server_default=text("''::character varying"))
