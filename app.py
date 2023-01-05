import requests
import pymongo
from flask import Flask, render_template, request, jsonify
import connect as c
from bson.binary import Binary
import base64
import io
from flask_restful import Resource, Api, reqparse
import werkzeug
import json
from PIL import Image
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html",med_clg_list=get_med_list()) 

def get_med_list():
    client = c.connectdb()
    db = client.get_database("NMCVideoAnalytic")
    collection = db.MedicalCollege
    allData  = collection.find()
    med_clg_list = []
    for i in allData:
        med_clg_list.append(i["Medical College"])  
    return med_clg_list

@app.route('/count', methods=['GET','POST'])
def countdf():
    print("Inside Count Function")
    headers = {
    'accept': 'application/json',
    }

    med_clg_list=get_med_list() 
    medicle_college = request.form.get("medicalcollegelist")
    camera_location_area = request.form.get("CameraLocationArea")
    camera_location_sub_area = request.form.get("CameraLocationSubArea")
    date_and_time = request.form.get("Test_DatetimeLocal")
    datetime_object = datetime.strptime(date_and_time, "%Y-%m-%dT%H:%M")
    #file = request.files.get("uploadfile")
    client = c.connectdb()
    db = client.get_database("NMCVideoAnalytic")
    images = db.nmcimages
    image = images.find()
    imagename = []
    counts = []
    imageview=[]
    for i in image : 
        files = {
        'img': ('img.jpg',i.__getitem__("data")),
        }
        if i.__getitem__("count") is None:
            response = requests.post('http://localhost:5008/api/v1/headcount', files=files)
            count = json.loads(response.text)
            count = count.__getitem__("head-count")
            filtr = {"imagename":i.__getitem__("imagename")}
            updtval = {"$set":{"count":count}} 
            db.nmcimages.update_one(filtr,updtval)
        else :
            count = i.__getitem__("count")
        imagename.append(i.__getitem__("imagename"))
        imagev = base64.b64encode(i.__getitem__("data"))
        imagev = imagev.decode('utf-8')
        imagev = "data:image/jpeg;base64," + imagev
        imageview.append(imagev)
        counts.append(count)
    length = len(counts)
    #pil_img = Image.open(io.BytesIO(image['data']))
    # parse = reqparse.RequestParser()
    # parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    # args = parse.parse_args()
    # image_file = args['file']
    # with open('test.png', 'wb') as f:
    #     f.write(image_file)
    # im_binary = base64.b64decode(uploadfile.stream)
    # buf = io.BytesIO(im_binary)
    #encoded = Binary(uploadfile.stream._file)
    #count=2
    # print(medicle_college)
    # print(camera_location)
    # print(date_and_time)
    
    #result = request.form

    #print(result)
    #return medicle_college,camera_location,date_and_time
    # params = {
    # 'input': '2',
    # }

    # headers = {
    # 'accept': 'application/json',
    # # requests won't add a boundary if this header is set when you pass files=
    # # 'Content-Type': 'multipart/form-data',
    # }

    # files = {
    #     'img': ('img.jpg',file),
    # }
    # filename=file.filename
    # response = requests.post('http://localhost:5008/api/v1/headcount', files=files)
    # count = json.loads(response.text)
    # count = count.__getitem__("head-count")
    # print(count)
    # counts = ['5','6']
    # imagename = ["abc.png","pqr.png"]
    # length = 2
    #return render_template('thankyou.html', medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=date_and_time,count=counts,filename=imagename,length=length,imageview=imageview) 
    return render_template('index.html', med_clg_list=med_clg_list,medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=datetime_object,count=counts,filename=imagename,length=length,imageview=imageview) 
    #return jsonify( med_clg_list=med_clg_list,medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=datetime_object,count=counts,filename=imagename,length=length,imageview=imageview)
@app.route('/back', methods=['GET','POST'])
def back():
    ret  = hello_world()
     #return render_template('index.html')
    return ret

@app.route("/cameraArea",methods=["POST","GET"])
def cameraArea():  

    if request.method == 'POST':
        medicalcollegelistValue = request.form['medicalcollegelistValue'] 
        client = c.connectdb()
        db = client.get_database("NMCVideoAnalytic")
        collection = db.MedicalCollege
        ls  = collection.find({"Medical College" : medicalcollegelistValue})
        nw = []
        for i in ls:
            # outputObj = {
            #     'name': i["Area"]}
            nw.append(i["Area"])

    return jsonify(nw)
    
@app.route("/cameraSubArea",methods=["POST","GET"])
def cameraSubArea():  

    if request.method == 'POST':
        medicalcollegelistValue = request.form['medicalcollegelistValue'] 
        
        CameraLocationAreaValue = request.form['CameraLocationAreaValue'] 
        client = c.connectdb()
        db = client.get_database("NMCVideoAnalytic")
        collection = db.MedicalCollege
        ls  = collection.find({"Medical College" : medicalcollegelistValue})
        nw = []
        for i in ls:
            # outputObj = {
            #     'name': i["Area"]}
            nw.append(i[CameraLocationAreaValue])

    return jsonify(nw)

if __name__ == "__main__":
    app.run(debug=True,port=8001)