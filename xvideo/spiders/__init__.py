
from xvideo.settings import MONGODB
from urllib import parse
from pymongo import MongoClient


def mongoclient():
    user = parse.quote_plus(MONGODB['MONGO_USER'])
    password = parse.quote_plus(MONGODB['MONGO_PASSWORD'])
    client =  MongoClient('mongodb://%s:%s@%s' % (user, password, MONGODB['MONGO_HOST']))[MONGODB['MONGO_DB']]
        # 执行数据上报
    return client

def getsite1():
    talbe = MONGODB['MONGO_TABLE']

    res = mongoclient()[talbe].find({"site":1})

    return res