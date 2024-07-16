
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')

def home():
    return 'hello, world'

@app.route('/bananas')

def home2():
    return 'This page has bananas'

@app.route('/bread')
def home3():
    return 'This page has bread!'

if __name__ == '__main__':
    app.run(debug=True)
