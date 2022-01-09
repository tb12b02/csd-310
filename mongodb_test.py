from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.e5jmi.mongodb.net/PyTech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.PyTech
print("\n --PyTech Collection List --")
print(db.list_collection_names())
input("\n\n End of program.. Press any key to EXIT... ")