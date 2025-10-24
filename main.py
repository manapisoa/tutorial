import uvicorn
from fastapi import FastAPI,Path,Body,Form,UploadFile,File,Cookie,Header
from fastapi.responses import JSONResponse
from typing import Optional

from pydantic import BaseModel,Field
app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello world"}

@app.get("/hello")
async def hello(name:str,age:int):
    return{"name":name,"age":age}

@app.get("/hello/{name}")
async def bonjour(name:str=Path(...,min_length = 3,max_length=10)):
    return {"name":name}

#pydantic
# class Student(BaseModel):
#     id:int
#     #name:str
#     name:str = Field(None,title="Decription de l'item" ,max_length = 10)
#     subject:list[str] = []

# data = {
#     'id':1,
#     'name':'karatra ',
#     'subject':['Enl','Zya','Grave']
# }
# S1 = Student(**data)

# @app.post("/entudiant/")
# async def etudiant(S1:Student):
#     return S1

# @app.post('/etudiant/')
# async def Etudiant(name:str=Body(...),marls:int=Body(...)):
#     return {"name":name,"marls":marls}

# @app.post("/etudiant/{college}")
# async def student(college:str,age:int,student:Student):
#     retval = {"college":college,"age":age,"student": student}
#     return retval

# use Class Pydantic as response model
class User(BaseModel):
    username: str
    password: str

@app.post("/submit/",response_model=User)
async def submit(nm:str = Form(...),pwd:str = Form(...) ):
    return User(username=nm , password=pwd)

#upload File
# @app.post("/upload/")
# async def upload_file(file:UploadFile = File(...)):


@app.post("/cookies/")
def createCookies():
    content = {"message":"cookie set"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username",value="admin")
    return response

#coockies
@app.get("/readCookies/")
async def read_cookies(username:str = Cookie(None)):
    return {"username":username}

@app.get("/header/")
async def read_header(accept_language:Optional[str] = Header(None)):
    return {"accept_langage":accept_language}
    
if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)


