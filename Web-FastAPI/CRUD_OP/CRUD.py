from fastapi import FastAPI , Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()




class Book(BaseModel):
    id:int
    name:str
    author:str 
    pages:int
    price:float

data = []


@app.post("/book")
async def add_new_book(b:Book):
    data.append(b)
    return b

@app.get("/get_books")
async def get_all():
    return data 


@app.get("/get_book/{book_id}")
async def get_book(book_id:int):      
    print(book_id)
    for i in range(len(data)): 
        print(data[i])
        if data[i].id == book_id:
            return data[i]  
    return "Not Found!"    
            

@app.put("/Edit_book/{book_id}")
async def edit_book(book_id:int , b:Book):
    for i in range(len(data)): 
        if data[i].id == book_id:
            data[i] = b 
            return b       
    return "Not found!"


@app.delete("/delete_book/{book_id}")
async def Delete_book(book_id:int):
    for i in range(len(data)): 
        if data[i].id == book_id:
            #print(data[i])
            data.pop(i)
            return "Deleted!"    
    return "Not found!"