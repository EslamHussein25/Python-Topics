from fastapi import FastAPI , Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []

@app.post("/students/")
async def student_data(s1: Student):
   print(s1)
   return s1

@app.post("/students_body/")
async def student_data(name:str = Body() , marks:int=Body()):
   return {f"name: {name} , marks: {marks}"}

@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/home")
def home():
    return {"mesaage" : "Hello Eslam from home"}


@app.post("/post/{name}")
def posting(name):
    return {f"name:{name} - age:{20}"}


# to run the server using this command 
# uvicorn main:app --reload
