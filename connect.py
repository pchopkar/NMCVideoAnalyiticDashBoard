import pymongo

def connectdb() :
#if __name__=="__main__":
    print("Insert connect.py")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connect Done at :" + str(client))
    return client

def connectatlasdb():
    print("Inside Atlas connect function")
    
    client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
    #db = client.test

    #client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
    print("Connect Done at :" + str(client))
    print(client.list_database_names())
    return client

 
#client = connectatlasdb()
client = connectdb()
db = client.get_database("NMCVideoAnalytic")
collection = db.MedcalCollege
#dictionary = {"Full Name" : "Parjanya Chopkar", "Email" : "chopkarparjanya@gmail.com", "Message" : "Hello World"}
#You have to create one dictionary for mat object and insert one row then only you can see table on mongoDb compass
#collection.insert_one(dictionary)

# collection.insert_many([
#    {
#       "Medical College": "Delhi Medical College",
#       "Area" : ["OPD","Lab","LectureHall","Department"],
#       "OPDArea": [ "Area 1","Area 2", "Area 3"],
#       "LabArea": [ "Area 4","Area 5", "Area 6"],
#       "LectruHallArea": [ "Area 7","Area 8", "Area 9"],
#        "DepartmentArea": [ "Area 10","Area 11", "Area 12"],
#    },
#      {
#       "Medical College": "Nagpur Medical College",
#       "Area" : ["OPD","Lab","LectureHall","Department"],
#       "OPDArea": [ "Area 1","Area 2", "Area 3"],
#       "LabArea": [ "Area 4","Area 5", "Area 6"],
#       "LectruHallArea": [ "Area 7","Area 8", "Area 9"],
#        "DepartmentArea": [ "Area 10","Area 11", "Area 12"],
#    },
#      {
#       "Medical College": "Mumbai Medical College",
#       "Area" : ["OPD","Lab","LectureHall","Department"],
#       "OPDArea": [ "Area 1","Area 2", "Area 3"],
#       "LabArea": [ "Area 4","Area 5", "Area 6"],
#       "LectruHallArea": [ "Area 7","Area 8", "Area 9"],
#        "DepartmentArea": [ "Area 10","Area 11", "Area 12"],
#    },
#      {
#       "Medical College": "Bhopal Medical College",
#       "Area" : ["OPD","Lab","LectureHall","Department"],
#       "OPDArea": [ "Area 1","Area 2", "Area 3"],
#       "LabArea": [ "Area 4","Area 5", "Area 6"],
#       "LectruHallArea": [ "Area 7","Area 8", "Area 9"],
#        "DepartmentArea": [ "Area 10","Area 11", "Area 12"],
#    }
# ])
# print("Inserted Successfully")

ls  = collection.find({"Medical College":""})
for i in ls:
    print(ls)
print(type(ls))