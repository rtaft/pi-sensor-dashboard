# coding: utf-8
from sqlalchemy import CHAR, Column, Date, Float, ForeignKey, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Reading(Base):
    __tablename__ = 'reading'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer) # TODO foreign key
    reading_time = Column(TIMESTAMP)
    value = Column (Float)

class SensorMapping(Base):
    __tablename__ = 'sensor_map'
    sensor_id =  Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(32), name="uuid", unique=True)
    