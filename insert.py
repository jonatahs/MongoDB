"""
*** Realizar insert ha duas formas, insertOne() e insertMany().

*** InsertOne() Insere apenas um documento e o Many varios documentos.

*** Caso nao especifique o ID de insercao o mongo gerara um automaticamente.
"""

# imports necessarios
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# conectando no banco de dados
client = MongoClient('mongodb+srv://ACCOUNT:PASSWORD@cluster0.zwytslc.mongodb.net/')

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Documento
myDocment = {
    'account_id': 794890,
    'limit': 14000,
    'products': [
                 "teste",
                 "Brokerage"
                 ],
                 "last_updated": '2023-05-14'}

# realizando insert

result = client['CRUD']['CRUD'].insert_one(myDocment)
#imprimindo o ID
print(f'Insercai feita com sucesso ID: {result.inserted_id}' )

# Realizando INSERT MANY

myManyDoc = [
    {
    'account_id': 11111,
    'limit': 14000,
    'products': [
                 "Many",
                 "Brokerage"
                 ],
                 "last_updated": '2023-05-14'},
    {
    'account_id': 222222,
    'limit': 14000,
    'products': [
                 "Many 2",
                 "Brokerage"
                 ],
                 "last_updated": '2023-05-14'},
    {
    'account_id': 333333,
    'limit': 14000,
    'products': [
                 "Many 3",
                 "Brokerage"
                 ],
                 "last_updated": '2023-05-14'}
                 ]

# realizando insert

result = client['CRUD']['CRUD'].insert_many(myManyDoc)
#imprimindo o ID
print(f'Insercao feita com sucesso ID: {result.inserted_ids}')
