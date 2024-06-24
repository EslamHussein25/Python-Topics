from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import List
from pydantic import BaseModel, constr
from fastapi import FastAPI, Depends



SQLALCHEMY_DATABASE_URL = 'postgresql://eslamsql:1234@127.0.0.1:5432/dbeslam'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False} , pool_pre_ping=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Books(Base):
   __tablename__ = 'book'
   id = Column(Integer, primary_key=True, nullable=False)
   title = Column(String(50), unique=True)
   author = Column(String(50))
   published_year = Column(String(50))
   Base.metadata.create_all(bind=engine) #The create_all() method creates the corresponding tables in the database.


class Book(BaseModel):
   id: int
   title: str
   author:str
   published_year: str
   class Config:
      orm_mode = True # Note: the use of orm_mode=True in the config class indicating that it is mapped with the ORM class of SQLAlchemy.





app=FastAPI()

def get_db():
   db = session()
   try:
      yield db
   finally:
            db.close()

@app.post('/add_book')
def Add_book(b1: Book, db: Session = Depends(get_db)):
   bk=Books(id=b1.id, title=b1.title, author=b1.author,published_year=b1.published_year)
   db.add(bk)
   db.commit()
   db.refresh(bk)
   return "Added"