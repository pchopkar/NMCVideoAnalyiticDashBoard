import pymongo
from PIL import Image
import io
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
collection = db.MedicalCollege
#dictionary = {"Full Name" : "Parjanya Chopkar", "Email" : "chopkarparjanya@gmail.com", "Message" : "Hello World"}
#You have to create one dictionary for mat object and insert one row then only you can see table on mongoDb compass
#collection.insert_one(dictionary)

# collection.insert_many([
#    {
#       "Medical College": "Delhi Medical College",
#       "Area" : ["Main Entrance","Patient Registration Counter","Lecture Theatre","Lab","OPD","Emergency & Casualty Ward","OT","Patient Attendant Waiting Area","Faculty Lounge","Attendance marking area"],
#       "Main Entrance": ["Camera 1", "Camera 2"],
#       "Patient Registration Counter": ["Camera 1", "Camera 2"],
#       "Lecture Theatre": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Lab": ["Anatomy Dissection Hall", "Physiology Lab", "Bio Chemistry UG Lab", "Pathology Lab", "Microbiology Lab", "Pharmocology Lab"],
#       "OPD": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Emergency & Casualty Ward": ["Camera 1", "Camera 2"],
#        "OT": ["Pre- Anaesthetia area", "Recovery Area"],
#        "Patient Attendant Waiting Area": ["Camera 1", "Camera 2"],
#        "Faculty Lounge": ["Camera 1", "Camera 2"],
#        "Attendance marking area": ["Camera 1", "Camera 2"],   
#    },
#       {
#       "Medical College": "Nagpur Medical College",
#       "Area" : ["Main Entrance","Patient Registration Counter","Lecture Theatre","Lab","OPD","Emergency & Casualty Ward","OT","Patient Attendant Waiting Area","Faculty Lounge","Attendance marking area"],
#       "Main Entrance": ["Camera 1", "Camera 2"],
#       "Patient Registration Counter": ["Camera 1", "Camera 2"],
#       "Lecture Theatre": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Lab": ["Anatomy Dissection Hall", "Physiology Lab", "Bio Chemistry UG Lab", "Pathology Lab", "Microbiology Lab", "Pharmocology Lab"],
#       "OPD": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Emergency & Casualty Ward": ["Camera 1", "Camera 2"],
#        "OT": ["Pre- Anaesthetia area", "Recovery Area"],
#        "Patient Attendant Waiting Area": ["Camera 1", "Camera 2"],
#        "Faculty Lounge": ["Camera 1", "Camera 2"],
#        "Attendance marking area": ["Camera 1", "Camera 2"],   
#    },
#       {
#       "Medical College": "Bhopal Medical College",
#       "Area" : ["Main Entrance","Patient Registration Counter","Lecture Theatre","Lab","OPD","Emergency & Casualty Ward","OT","Patient Attendant Waiting Area","Faculty Lounge","Attendance marking area"],
#       "Main Entrance": ["Camera 1", "Camera 2"],
#       "Patient Registration Counter": ["Camera 1", "Camera 2"],
#       "Lecture Theatre": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Lab": ["Anatomy Dissection Hall", "Physiology Lab", "Bio Chemistry UG Lab", "Pathology Lab", "Microbiology Lab", "Pharmocology Lab"],
#       "OPD": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Emergency & Casualty Ward": ["Camera 1", "Camera 2"],
#        "OT": ["Pre- Anaesthetia area", "Recovery Area"],
#        "Patient Attendant Waiting Area": ["Camera 1", "Camera 2"],
#        "Faculty Lounge": ["Camera 1", "Camera 2"],
#        "Attendance marking area": ["Camera 1", "Camera 2"],   
#    },
#       {
#       "Medical College": "Kolkata Medical College",
#       "Area" : ["Main Entrance","Patient Registration Counter","Lecture Theatre","Lab","OPD","Emergency & Casualty Ward","OT","Patient Attendant Waiting Area","Faculty Lounge","Attendance marking area"],
#       "Main Entrance": ["Camera 1", "Camera 2"],
#       "Patient Registration Counter": ["Camera 1", "Camera 2"],
#       "Lecture Theatre": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Lab": ["Anatomy Dissection Hall", "Physiology Lab", "Bio Chemistry UG Lab", "Pathology Lab", "Microbiology Lab", "Pharmocology Lab"],
#       "OPD": [ "Medicine","Surgical", "Gynaecological", "Paediatrics","Ortho"],
#       "Emergency & Casualty Ward": ["Camera 1", "Camera 2"],
#        "OT": ["Pre- Anaesthetia area", "Recovery Area"],
#        "Patient Attendant Waiting Area": ["Camera 1", "Camera 2"],
#        "Faculty Lounge": ["Camera 1", "Camera 2"],
#        "Attendance marking area": ["Camera 1", "Camera 2"],   
#    }
# ])
# print("Inserted Successfully")

# medical_college="Nagpur Medical College"
# ls  = collection.find({"Medical College" : medical_college})
# nw = []
# for i in ls:
#     nw.append(i["Area"])

# print(nw)
# for i in ls:
#     print(i)
#     print(i["Medical College"])
#     nw.append(i["Medical College"]["Area"])
# collection.insert_many([
#    {
#       "Medical College": "Delhi Medical College",
#       "Area" : ["Main Entrance","Patient Registration Counter","Lecture Theatre","Lab","OPD","Emergency & Casualty Ward","OT","Patient Attendant Waiting Area","Faculty Lounge","Attendance marking area"],
#       "OPDArea": [ "Area 1","Area 2", "Area 3"],
#       "LabArea": [ "Area 4","Area 5", "Area 6"],
#       "LectruHallArea": [ "Area 7","Area 8", "Area 9"],
#        "DepartmentArea": [ "Area 10","Area 11", "Area 12"],
#    },
# ])

# images = db.nmcimages

# im = Image.open("NMC.png") 
# #image_bytes = io.BytesIO(im)
# #im.save(im, format='png')
# image = {
#     'data': im.getvalue()
# }

# image_id = images.insert_one(image).inserted_id
# print(image_id)
# print("Inserted Successfully")