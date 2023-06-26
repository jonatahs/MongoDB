"""
Para realizar o delete de um documento utilizamos o delete_one(), para muitos delete_many()

db.collection.delete_one(<fiter>)

"""

from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId

# conectando no banco de dados
client = MongoClient('')

try:
    print("\n")
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print("\n")
except Exception as e:
    print(e)

# coletando referencia do Banco
db = client.CRUD

# Referencia de colecao 
collection = db.CRUD

# Filter

document_to_delete = {"_id":ObjectId("64617191383aeff07aa867d1")}

# realizando o delete

result = collection.delete_one(document_to_delete)

print("Searching for target document after delete: ")
print(collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))


""""

DELETE MANY

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$lt": 2000}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()


"""
