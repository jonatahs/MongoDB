from connect import mongo

# gerando conexao 
client = mongo().cliente()

# get reference db
db = client.sample_analytics

# get collection reference

accounts_collection = db.accounts

# calculate the average limit accounts

select_by_limit = {"$match": {"limit":{"$lt": 10000}}}

# separate documents by account_id 

separete_by_account_id = {"$group":{"_id":"$account_id","limit":{"$sum":"$limit"}}}

# creating an agreggation

pipeline = [
    select_by_limit,
]

# performing an agreggation on `pipeline`

results = accounts_collection.aggregate(pipeline)

for i in results:
    print(i)