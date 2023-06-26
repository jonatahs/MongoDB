from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://jonatahs18:FkodOXfGl6xGLmku@cluster0.zwytslc.mongodb.net/"

def conect_mongo(uri):
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client


class mongo():
    def cliente(self):
        client = conect_mongo(uri)

        return client
        