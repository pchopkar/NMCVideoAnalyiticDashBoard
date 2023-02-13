import requests
from flask import Flask, render_template, request, jsonify
import connect as c
import base64
import json
from datetime import datetime
import logging
import time
import cv2
import numpy as np
import os
import io
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


def firstpage():
    return render_template("hello.html") 
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
   
        logging.info("Inside countdf() function")
        headers = {
        'accept': 'application/json',
        }

        med_clg_list=get_med_list() 
        medicle_college = request.form.get("medicalcollegelist")
        camera_location_area = request.form.get("CameraLocationArea")
        camera_location_sub_area = request.form.get("CameraLocationSubArea")
        date_and_time = request.form.get("Test_DatetimeLocal")
        datetime_object = ''
        imagename = []
        counts = []
        imageview=[]
        page = 'index.html'
        noRecordflag=True
        length = 0
        if medicle_college and camera_location_area and camera_location_sub_area and date_and_time :
            try: 
                datetime_object = datetime.strptime(date_and_time, "%Y-%m-%dT%H:%M")
                # date = datetime_object.strftime("%B %d, %Y")
                # timed = datetime_object.strftime("%I:%M %p")
                #timed= datetime.strptime(timed, "%I:%M %p")
                #file = request.files.get("uploadfile")
                # date = datetime.strptime(date_and_time, "%m/%d/%Y").date()
                # timed = datetime.strptime(date_and_time, "%I:%M %p").time()
                date = datetime_object.strftime('%B %d, %Y')
                timed = datetime_object.strftime('%H:%M')
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
            
                start = time.time()
                
                for i in image : 
                    files = {
                    'img': ('img.jpg',i.__getitem__("frame_data")),
                    }
                    if i.__getitem__("count") is None:
                        
                        response = requests.post('http://localhost:5008/api/v1/headcount', files=files)
                        #response=502
                        if (response.status_code >= 200 and response.status_code<=300):
                            #if(response.ok):
                            count = json.loads(response.text)
                            count = count.__getitem__("head-count")
                            filtr = {"imagename":i.__getitem__("image_name")}
                            updtval = {"$set":{"count":count}} 
                            db.nmcimages.update_one(filtr,updtval)      
                        else:
                            page='servicedown.html'
                            break
                    else :
                        count = i.__getitem__("count")
                    imagename.append(i.__getitem__("image_name"))
                    imagev = base64.b64encode(i.__getitem__("frame_data"))
                    imagev = imagev.decode('utf-8')
                    imagev = "data:image/jpe    g;base64," + imagev
                    imageview.append(imagev)
                    counts.append(count)
                    page='index.html'
                    noRecordflag=False
                if len(page) == 0:
                    page='index.html'
                    noRecordflag=True
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
        return render_template(page, med_clg_list=med_clg_list,medicle_college=medicle_college, camera_location_area=camera_location_area, camera_location_sub_area=camera_location_sub_area,date_and_time=datetime_object,count=counts,filename=imagename,length=length,imageview=imageview,noRecordflag=noRecordflag) 
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

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    client = c.connectdb()
    db = client.get_database("NMCVideoAnalytic")
    collection = db.nmcimages2
    if request.method == 'POST':
        video_file = request.files['video_file']
        video_path = "C:\\Users\\Administrator\\Desktop\\NMCVideoAnalyiticDashBoard"
        video_file.save(f"{video_path}/{video_file.filename}")

        # Open the video using OpenCV
        video = cv2.VideoCapture(f"{video_path}/{video_file.filename}")
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Get the video frame rate
        fps = video.get(cv2.CAP_PROP_FPS)

        # Calculate the number of frames to skip between each output frame
        skip_frames = int(fps / 15)

        # Get the video's name
        video_name = video_file.filename
        
        # Initialize frame counter
        frame_count = 0

        while True:
            # Read a frame from the video
            ret, frame = video.read()

            # Break the loop if we've reached the end of the video
            if not ret:
                break

            # Only save every nth frame
            if frame_count % skip_frames == 0:
                # Encode the frame in JPEG format
                _, frame_buf = cv2.imencode('.jpg', frame)

                # Convert the image to binary
                frame_binary = frame_buf.tobytes()

                now = datetime.utcnow()
                date = now.strftime("%B %d, %Y")
                timed = now.strftime("%I:%M %p")
                # Create a document to insert into MongoDB
                document = {
                    "frame_number": frame_count,
                    "imagename": video_name,
                    "data": frame_binary,
                    "count" : None,
                    "date": date,
                    "time": timed,
                    "medicle_college" : "Nagpur Medical College",
                    "camera_location_area" : "OPD",
                    "camera_location_sub_area" : "Gynaecological"
                }
                # Insert the document into MongoDB
                collection.insert_one(document)
            # Increment the frame counter
            frame_count += 1

        # Release the video file
        video.release()
        if os.path.isfile(f"{video_path}/{video_file.filename}"):
            os.remove(f"{video_path}/{video_file.filename}")
    return render_template("success.html") 

if __name__ == "__main__":
    app.run(debug=True,port=8001)