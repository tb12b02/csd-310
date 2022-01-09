from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.e5jmi.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print("\n --PyTech Collection List --")
print(db.list_collection_names())
input("\n\n End of program.. Press any key to EXIT... ")