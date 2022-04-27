from typing import Optional
from unicodedata import name
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 
from fastapi import FastAPI, Request, Body, File, UploadFile, Form

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # create database and table if it does not already exist


templates = Jinja2Templates(directory="templates")
mylist = []


#utility function to handle the opening and closing of database engine automatically
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# structure user input
class FormData(BaseModel):
    first_name : str
    last_name : str
    birthday : str
    filename : str

# render home page
@app.get("/home", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


# Endpoit for submitting form data
@app.post("/submitform")
async def handle_form(first_name: str = Form(...), last_name: str = Form(...), birthday: str = Form(...), filename: str = Form(...)):
    mylist.append(first_name)
    mylist.append(last_name)
    mylist.append(birthday)
    mylist.append(filename)
    print(mylist)
    print(type(birthday))
    print(type(filename))




