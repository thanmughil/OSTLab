from pymongo import MongoClient

def ConnectToDB():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["OST5b"]
    return database

database = ConnectToDB()
collection = database["Student_Details"]
columns = ["Name","RollNo","Gender","CGPA","eMail","PhoneNo"]

def viewRecords(collection):
    records = collection.find({})
    for record in records:
        for i,j in list(record.items())[1:]:
            print(f"{i} : {j}")
        print()

def addRecord(collection):
    record = {}
    for i in columns:
        record[i] = input(f"Enter {i}: ")
    record["CGPA"] = float(record["CGPA"])
    collection.insert_one(record)

while True:
        print("\nMenu:")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Enter your choice: ")
        print("\n")

        if choice == '1':
            addRecord(collection)
        elif choice == '2':
            viewRecords(collection)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")