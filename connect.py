import pymongo
import io
import base64
from datetime import datetime, time
import logging
from PIL import Image
logging.basicConfig(level=logging.INFO)
def connectdb() :
#if __name__=="__main__":
    try:
        logging.info("Inside connectdb()")
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        logging.info("Done of connectdb()")
    except Exception as e:
        print(e)
        logging.info("Inside exception of connectdb()")
    return client

def connectatlasdb():
    print("Inside Atlas connect function")
    try :
        client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
        print("Connect Done at :" + str(client))
    except Exception as e:
        print(e)

    return client

 
# client = connectatlasdb()
client = connectdb()
db = client.get_database("NMCVideoAnalytic")
# collection = db.MedicalCollege
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


#Important to insert images

# images = db.nmcimages
# #Image1
# now = datetime.utcnow()
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
# print("Inserted 1")

# #Image2
# now = datetime.utcnow()
# date = now.strftime("%B %d, %Y")
# timed = now.strftime("%I:%M %p")
# im = Image.open("NMC.png") 
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
# print("Inserted 2")

# #Image3
# now = datetime.utcnow()
# date = now.strftime("%B %d, %Y")
# timed = now.strftime("%I:%M %p")
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
# print("Inserted 3")

# #Image4
# now = datetime.utcnow()
# date = now.strftime("%B %d, %Y")
# timed = now.strftime("%I:%M %p")
# im = Image.open("opd.jpg") 
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
# print("Inserted 4")













