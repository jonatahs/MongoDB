from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://jonatahs18:FkodOXfGl6xGLmku@cluster0.zwytslc.mongodb.net/"

def conect_mongo(uri):
    client = MongoClient(uri)

    return client


class mongo():
    def cliente(self):
        client = conect_mongo(uri)

        return client
        