import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.e5jmi.mongodb.net"
ca = certifi.where()
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech
print("\n --PyTech Collection List --")
print(db.list_collection_names())
input("\n\n End of program.. Press any key to EXIT... ")