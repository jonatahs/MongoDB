# generate and importing the connection 
from connect import mongo
client = mongo().cliente()

db = client.sample_analytics

collection = db.transactions

# Organize documents with sort
# To sort ASC use 1
# To sort DESC use -1

organize_transaction_counts = {"$sort":{"transaction_count": -1}}

# using project

return_specified_fields = {
    "$project": {
        "account_id": 1,
        "transaction_count":-1
    }
}

pipeline = [
    organize_transaction_counts,
    return_specified_fields
    ]

results = collection.aggregate(pipeline)

for i in results:
    print(i)