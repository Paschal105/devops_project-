# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"

if __name__ == '__main__':
    app.run(host='5000', port=5000, debug=True)