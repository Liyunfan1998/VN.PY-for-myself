# coding=utf-8 
from pymongo import MongoClient 
import pandas as pd 
class MongoDbHandler(object): 
    def __init__(self, ip, user=None, keyword=None): 
        if user == None or keyword == None: 
            URL = 'mongodb://{0}'.format(ip) 
        else: 
            URL = 'mongodb://{0}:{1}@{2}'.format(user, keyword, ip) 
        print user,keyword 
        print URL 
        self.__Client = MongoClient(URL)
    def find_all(self, db, collection, condition = None): 
        self.__db = self.__Client[db] 
        self.__collection = self.__db[collection] 
        cursor = self.__collection.find(condition) 
        result = [] 
        for contentDict in cursor: 
            result.append(contentDict) 
        return result 
    def find_all_cursor(self, db, collection, condition = None): 
        self.__db = self.__Client[db] 
        self.__collection = self.__db[collection] 
        cursor = self.__collection.find(condition) 
        return cursor 
    def insert_one(self, db, collection, jsonData): 
        _db = self.__Client[db] 
        _collection = _db[collection] 
        result = _collection.insert_one(jsonData) 
    def insert_many(self, db, collection, jsonData): 
        _db = self.__Client[db] 
        _collection = _db[collection] 
        result = _collection.insert_many(jsonData) 
        return result 
    def drop(self,db,collection): 
        _db = self.__Client[db] 
        _collection = _db[collection] 
        _collection.drop() 
    def close(self): 
        return self.__Client.close() 
