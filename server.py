from flask import Flask
from flask import request
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=['POST'])
def send():
    data = request.get_json()
    count = 0
    print(data['files'])
    with open('number.txt', 'r') as file:
        content = file.read()
        count = int(content)
        count+=1

    with open('number.txt', 'w') as file:
        file.write(f'{count}')
    
    f = data['files']

    with open(f'files/{count}.txt', 'x') as file:
        file.write(f'{f}')

    return "file Uploaded Successfully"

@app.route('/')
def home():
    print('hello')
    return 'hi'
