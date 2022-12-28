import requests
import pymongo
from flask import Flask, render_template, request
import connect as c


app = Flask(__name__)
@app.route('/')
def hello_world():
    client = c.connectdb()
    db = client.get_database("NMCVideoAnalytic")
    collection = db.MedcalCollege
    allData  = collection.find()
    med_clg_list = []
    for i in allData:
        med_clg_list.append(i["Medical College"])    

    return render_template("index.html",med_clg_list=med_clg_list) 

@app.route('/count', methods=['GET','POST'])
def count():
    print("Inside Count Function")
    headers = {
    'accept': 'application/json',
    }


    # medicle_college = request.form.get("Medicle College")
    # camera_location = request.form.get("Camera Location")
    # date_and_time = request.form.get("Date and Time")
    
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

    headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'img': open('NMC.png;type=image/png', 'rb'),
    }

    response = requests.post('http://localhost:5008/api/v1/headcount', headers=headers, files=files)
    count=response.text
    return render_template('index.html', medicle_college=medicle_college, camera_location=camera_location,date_and_time=date_and_time,count=count) 

@app.route('/back', methods=['GET','POST'])
def back():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,port=8001)