import requests
from flask import Flask, render_template, request, jsonify
import connect as c
import base64
import json
from datetime import datetime
import logging
import time
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
@app.route('/')
def indexpage():
    logging.info("Opening Index.html")
    return render_template("index.html",med_clg_list=get_med_list()) 

def get_med_list():
    try:
        logging.info("Inside get_med_list()")
        client = c.connectdb()
        db = client.get_database("NMCVideoAnalytic")
        collection = db.MedicalCollege
        allData  = collection.find()
        med_clg_list = []
        for i in allData:
            med_clg_list.append(i["Medical College"])
        logging.info("Done from get_med_list()")
    except Exception as e:
        print(e)
        logging.info("Inside exception of get_med_list()")
    finally:
        client.close()
    return med_clg_list

@app.route('/count', methods=['GET','POST'])
def countdf():
    try:
        logging.info("Inside countdf() function")
        headers = {
        'accept': 'application/json',
        }

        med_clg_list=get_med_list() 
        medicle_college = request.form.get("medicalcollegelist")
        camera_location_area = request.form.get("CameraLocationArea")
        camera_location_sub_area = request.form.get("CameraLocationSubArea")
        date_and_time = request.form.get("Test_DatetimeLocal")
        datetime_object = datetime.strptime(date_and_time, "%Y-%m-%dT%H:%M")
        date = datetime_object.strftime("%B %d, %Y")
        timed = datetime_object.strftime("%I:%M %p")
        #file = request.files.get("uploadfile")
        client = c.connectdb()
        db = client.get_database("NMCVideoAnalytic")
        images = db.nmcimages

        query = {
        "date": {
            "$eq": date
        },
        "time": {
            "$lte": timed
        },
        "medicle_college": {
            "$eq": medicle_college
        },
        "camera_location_area": {
            "$eq": camera_location_area
        },
        "camera_location_sub_area": {
            "$eq": camera_location_sub_area
        }
        }

        image = images.find(query)
        imagename = []
        counts = []
        imageview=[]
        start = time.time()
        page = ''
        for i in image : 
            files = {
            'img': ('img.jpg',i.__getitem__("data")),
            }
            if i.__getitem__("count") is None:
                
                response = requests.post('http://localhost:5008/api/v1/headcount', files=files)
                #response=502
                if (response.status_code >= 200 and response.status_code<=300):
                    #if(response.ok):
                    count = json.loads(response.text)
                    count = count.__getitem__("head-count")
                    filtr = {"imagename":i.__getitem__("imagename")}
                    updtval = {"$set":{"count":count}} 
                    db.nmcimages.update_one(filtr,updtval)      
                else:
                    page='servicedown.html'
                    break
            else :
                count = i.__getitem__("count")
            imagename.append(i.__getitem__("imagename"))
            imagev = base64.b64encode(i.__getitem__("data"))
            imagev = imagev.decode('utf-8')
            imagev = "data:image/jpe    g;base64," + imagev
            imageview.append(imagev)
            counts.append(count)
            page='index.html'
        if len(page) == 0:
            page='index.html'
        length = len(counts)
        end = time.time()
        total_time = end - start
        logging.info("Done from countdf()" + str(total_time))
    except Exception as e:
        print(e) 
        logging.info("Inside exception of countdf()")

    finally:
        client.close()
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
    return render_template(page, med_clg_list=med_clg_list,medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=datetime_object,count=counts,filename=imagename,length=length,imageview=imageview) 
    #return jsonify( med_clg_list=med_clg_list,medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=datetime_object,count=counts,filename=imagename,length=length,imageview=imageview)
@app.route('/back', methods=['GET','POST'])
def back():
    ret  = indexpage()
     #return render_template('index.html')
    return ret

@app.route("/cameraArea",methods=["POST","GET"])
def cameraArea():  
    try:
        logging.info("Inside of cameraArea()")
        if request.method == 'POST':
            medicalcollegelistValue = request.form['medicalcollegelistValue'] 
            client = c.connectdb()
            db = client.get_database("NMCVideoAnalytic")
            collection = db.MedicalCollege
            ls  = collection.find({"Medical College" : medicalcollegelistValue})
            nw = []
            for i in ls:
                nw.append(i["Area"])
            logging.info("Done of cameraArea()")
    except Exception as e:
        print(e)
        logging.info("Inside exception of cameraArea()")
    finally:
        client.close()
    return jsonify(nw)
    
@app.route("/cameraSubArea",methods=["POST","GET"])
def cameraSubArea():  
    try:
        logging.info("Inside of cameraSubArea()")
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
            logging.info("Done of cameraSubArea()")
    except Exception as e:
        print(e)
        logging.info("Inside exception of cameraSubArea()")
    finally:
        client.close()

    return jsonify(nw)

if __name__ == "__main__":
    app.run(debug=True,port=8001)