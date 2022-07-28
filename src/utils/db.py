import pymongo
import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')


class Db: 
    def __init__(self, url, db_name) :
        self.client = pymongo.MongoClient(url)
        self.db = self.client[db_name]

    def insert_data(self, col, data ):
        self.db[col].insert_one(data)


db = Db(DB_URL, DB_NAME)
