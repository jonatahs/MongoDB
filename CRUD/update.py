"""
Para realizar o update de um documento utilizamos o update_one(), para muitos update_many()

db.collection.update_one(<fiter>, <update>)

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


# Realizando find de um objeto

# result = client['CRUD']['CRUD'].find_one()

# referencia database
db = client.CRUD

# referencia da colecao

collection = db.CRUD

# filter

documento_to_update = {"_id": ObjectId("646170f9b9a87427f6b4a772")}

# update

# Acrecenta mais 15000
add_accountID = {"$inc":{"limit":15000}}

result = collection.update_one(documento_to_update, add_accountID)

print("Documents updated: " + str(result.modified_count))

"""
UPDATE MANY


# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
"""
