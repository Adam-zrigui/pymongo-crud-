from pymongo import MongoClient
import os

async def  db():
    try:
        myclient = MongoClient(os.environ['MONGO_URI'], serverSelectionTimeoutMS=5000)
        print("DB connection established")
        mydb = myclient["test"]
        mycol = mydb["users"]
        return mycol
    except Exception as e:
        print(f'error : {e}')
        raise e
