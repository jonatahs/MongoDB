"""
Para realizar o Read no MongoDB usamos o find(), utilizamos no seguinte formato : db.<collection>.find()

"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# conectando no banco de dados
client = MongoClient('mongodb+srv://ACCOUNT:PASSWORD@cluster0.zwytslc.mongodb.net/')

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

"""
Operadores Logicos MongoDB
$gt (maior que)
$gte(maior igual)
$lt (menos que )
$lte (menos ou igual)
$and
$or



Exemplos:
    $gt:
        db.sales.find({ "items.price": { $gt: 50}})
    $lt:
        db.sales.find({ "items.price": { $lt: 50}})
    $lte:
        db.sales.find({ "customer.age": { $lte: 65}})
    $gte:
        db.sales.find({ "customer.age": { $gte: 65}})
    
    $or:
        db.routes.find({
            $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }],
            })


        
======================================================

Realizando Querys em Arrays nos documentos no Mongo DB

Para acharmos valores em um objeto que tem array devemos usar o $elemMatch

Exemplos: 

db.account.find({
    products: {
        $elemMatch: {$eq: 'InvestmentStock'}
    }
})


db.sales.find({
  items: {
    $elemMatch: { name: "laptop", price: { $gt: 800 }, quantity: { $gte: 1 } },
  },
})

db.transactions.find({
    transactions: {
      $elemMatch: { amount: { $lte: 4500 }, transaction_code: "sell" },
    },
  })

"""

