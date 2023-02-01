from dotenv import load_dotenv
import sys
import asyncio
sys.path.append("./config/")
from db import db
load_dotenv(dotenv_path="./config/.env")
mycol = asyncio.run(db())

mycol.insert_many([
    {
        "username": 'adzrs',
         "age":18,
         "email": 'adzrs@gmail.com',
         "isAdmin": False      
    },
    {
        "username":"adzr",
        "age":18,
        "email": 'adz@gmail.com',
        "isAdmin": False
    },
    {
       "username": "admin", 
       "age": None,
       "email": "admin",
    }
])
mycol.find_one_and_update({"username": "adzrs"}, {"$set":{"age": 19 }})
mycol.find_one_and_delete({"username": "adzr"})
docs = list(mycol.find())
for doc in docs:
  print(doc)

