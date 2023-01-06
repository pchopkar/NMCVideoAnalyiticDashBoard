import pymongo
from PIL import Image
import io
import base64
import gridfs
from datetime import datetime, time
def connectdb() :
#if __name__=="__main__":
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
    except Exception as e:
        print(e)

    return client

def connectatlasdb():
    print("Inside Atlas connect function")
    try :
        client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print(e)

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


#Important to insert images
# images = db.nmcimages



# now = datetime.utcnow()
# #datetime_object = datetime.strptime(str(now), "%Y-%m-%d %H:%M:%S.S")
# date = now.strftime("%B %d, %Y")
# timed = now.strftime("%I:%M %p")
# im = Image.open("classroom.jpg") 

# image_bytes = io.BytesIO()
# im.save(image_bytes, format='png')

# image = {
#     'imagename' : im.filename,
#     'data': image_bytes.getvalue(),
#     'count' : None,
#     "date": date,
#     "time": timed
# }

# image_id = images.insert_one(image).inserted_id

# now = datetime.utcnow()
# im = Image.open("opd-inner.png") 

# image_bytes = io.BytesIO()
# im.save(image_bytes, format='png')

# image = {
#     'imagename' : im.filename,
#     'data': image_bytes.getvalue(),
#     'count' : None,
#     "date": date,
#     "time": timed
# }

# image_id = images.insert_one(image).inserted_id




# client = MongoClient()
# db = client.testdb

# images = db.images
# image = images.find()
# for i in image :
#      print(i)
# print("hello")
# pil_img = Image.open(io.BytesIO(image['data']))
# pil_img.imshow(pil_img)
# pil_img.show()


#db = db.nmcimages
# encode your image to binary text
# with open("classroom.jpg", "rb") as image:
#     # read the image as text and convert it to binary
#     image_string = base64.b64encode(image.read())
#     image_string = "data:image/jpeg;base64," + str(image_string)

# # create Gridfs instance
# fs = gridfs.GridFS(db, "fs")

# # add the image to your database
# put_image = fs.put(image_string, encoding='utf-8')