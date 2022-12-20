import requests
from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/count', methods=['GET','POST'])
def render():
    print("Inside Count Function")
    headers = {
    'accept': 'application/json',
    }

    # params = {
    # 'input': '2',
    # }
    response = requests.get('http://127.0.0.1:8000/apicount', headers=headers)
    #print(response.)
    return render_template('thankYou.html',messages=json.loads(response)) 

if __name__ == "__main__":
    app.run(debug=True,port=8000)