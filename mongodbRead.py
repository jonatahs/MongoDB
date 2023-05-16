"""
Para realizar o Read no MongoDB usamos o find(), utilizamos no seguinte formato : db.<collection>.find()

"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# conectando no banco de dados
client = MongoClient('mongodb+srv://jonatahs18:FkodOXfGl6xGLmku@cluster0.zwytslc.mongodb.net/')

try:
    print("\n")
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print("\n")
except Exception as e:
    print(e)


# Realizando find de um objeto

result = client['CRUD']['CRUD'].find_one()
print("\n")
print("----------------------------- FIND DE UM OBJETO -----------------------------")
print("\n")
print(result)

print("\n")
print("----------------------------- FIND DE TODO OS OBJETOS -----------------------------")
print("\n")
for i in client['CRUD']['CRUD'].find():
    print(i)

print("----------------------------- FILTRANDO FIND -----------------------------")

findFilter = client['CRUD']['CRUD'].find({},{'account_id': 794876})

print(findFilter)