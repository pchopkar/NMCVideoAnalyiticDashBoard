import requests
from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html") 

@app.route('/count', methods=['GET','POST'])
def count():
    print("Inside Count Function")
    headers = {
    'accept': 'application/json',
    }
    medicle_college = request.form.get("Medicle College")
    camera_location = request.form.get("Camera Location")
    date_and_time = request.form.get("Date and Time")
    count=2
    # print(medicle_college)
    # print(camera_location)
    # print(date_and_time)
    
    #result = request.form

    #print(result)
    #return medicle_college,camera_location,date_and_time
    # params = {
    # 'input': '2',
    # }
    response = requests.get('http://127.0.0.1:8000/apicount', headers=headers)
    #print(response.)
    return render_template('thankYou.html', medicle_college=medicle_college, camera_location=camera_location,date_and_time=date_and_time,count=count) 

@app.route('/back', methods=['GET','POST'])
def back():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000)