from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.e5jmi.mongodb.net/PyTech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.PyTech

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Gertrude = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

print("  Student ID: " + Gertrude["student_id"] + "\n  First Name: " + Gertrude["first_name"] + "\n  Last Name: " + Gertrude["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")

