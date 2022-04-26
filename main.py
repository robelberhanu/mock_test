from typing import Optional
from unicodedata import name
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
 
from fastapi import FastAPI, Request, Body, File, UploadFile, Form

app = FastAPI()


templates = Jinja2Templates(directory="templates")


# structure user input
class FormData(BaseModel):
    first_name : str
    last_name : str

# render home page
@app.get("/home", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


# Endpoit for submitting form data
@app.post("/submitform")
async def handle_form(first_name: str = Form(...)):
    print(first_name)



