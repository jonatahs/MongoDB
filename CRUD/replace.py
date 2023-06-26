from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# conectando no banco de dados
client = MongoClient('')

try:
    print("\n")
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print("\n")
except Exception as e:
    print(e)


"""
To replace documents in MongoDB, we use the replaceOne() method. The replaceOne() method takes the following parameters:

db.collection.replaceOne(filter,replacement,options)

filter: A query that matches the document to replace.
replacement: The new document to replace the old one with.
options: An object that specifies options for the update.

Ex.: 

db.books.replaceOne(
  {
    _id: ObjectId("6282afeb441a74a98dbbec4e"),
  },
  {
    title: "Data Science Fundamentals for Python and MongoDB",
    isbn: "1484235967",
    publishedDate: new Date("2018-5-10"),
    thumbnailUrl:
      "https://m.media-amazon.com/images/I/71opmUBc2wL._AC_UY218_.jpg",
    authors: ["David Paper"],
    categories: ["Data Science"],
  }
)

"""



