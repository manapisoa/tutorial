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

# #upload File
# # @app.post("/upload/")
# # # async def upload_file(file:UploadFile = File(...)):


# @app.post("/cookies/")
# def createCookies():
#     content = {"message":"cookie set"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key="username",value="admin")
#     return response

# #coockies
# @app.get("/readCookies/")
# async def read_cookies(username:str = Cookie(None)):
#     return {"username":username}

# @app.get("/header/")
# async def read_header(accept_language:Optional[str] = Header(None)):
#     return {"accept_langage":accept_language}


#relation pydantique
# class Student(BaseModel):
#     id : int
#     name :str = Field(None,title="name of student", max_length=10)
#     marks: list[int] = []
#     precent_mark: float

# class Precent(BaseModel):
#     id : int
#     name : str = Field(None,title="name of student " , max_length=10)
#     precent_marks: float

# @app.post('/marks')
# async def get_precent(s1:Student):
#     s1.precent_mark = sum(s1.marks)
#     return s1

#related class Pydantic
# class Supplier(BaseModel):
#     supplierId: int
#     supplierName : str

# class Product(BaseModel):
#     productId: int
#     productName:str
#     price:int
#     productSupplier:Supplier

# class customer(BaseModel):
#     customerId: int
#     customerName: str
#     prod:tuple[Product]

# @app.post('/invoice')
# async def getInvoice(c1:customer):
#     return c1

# async def dependancy(id:str,name:str):
#     return{'id':id,"name":name}

# @app.get("/user/")
# async def user(dep:dict = Depends(dependancy)):
#     return dep


data = []
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher : str

@app.post("/books/")
async def add_book(book:Book):
    data.append(book.dict())
    return data

@app.put("/books/{id}")
async def update_book(id:int,book:Book):
    data[id-1] = book
    return data

@app.get("/book/")
def getBook():
    return data

@app.delete("/book/{id}")
async def delete_book(id:int):
    data.pop(id-1)
    return data


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)


