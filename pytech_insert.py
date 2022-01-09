from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.e5jmi.mongodb.net/PyTech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.PyTech
Gertrude = {
    "student_id": "1007",
    "first_name": "Gertrude",
    "last_name": "Stallings",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "November 29, 2021",
            "end_date": "March 06, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR305",
                    "description": "Web, Commerce and Application Security",
                    "instructor": "Professor Donoho",
                    "grade": "A+"
                }
            ]
        }
    ]

}

Ethel = {
    "student_id": "1008",
    "first_name": "Ethel",
    "last_name": "Manerski",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "November 29, 2021",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "B+"
                },
                {
                    "course_id": "CYBR305",
                    "description": "Web, Commerce and Application Security",
                    "instructor": "Professor Donoho",
                    "grade": "A-"
                }
            ]
        }
    ]
}

Bertha = {
    "student_id": "1009",
    "first_name": "Bertha",
    "last_name": "Kranz",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "November 29, 2021",
            "end_date": "March 6, 2022",
            "courses": [
 {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "C"
                },
                {
                    "course_id": "CYBR305",
                    "description": "Web, Commerce and Application Security",
                    "instructor": "Professor Donoho",
                    "grade": "C"
                }
            ]
        }
    ]
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
Gertrude_student_id = students.insert_one(Gertrude).inserted_id
print("  Inserted student record Gertrude Stallings into the students collection with document_id " + str(Gertrude_student_id))

Ethel_student_id = students.insert_one(Ethel).inserted_id
print("  Inserted student record Ethel Manerski into the students collection with document_id " + str(Ethel_student_id))

Bertha_student_id = students.insert_one(Bertha).inserted_id
print("  Inserted student record Bertha Kranz into the students collection with document_id " + str(Bertha_student_id))

input("\n\n End of program.. Press any key to EXIT... ")