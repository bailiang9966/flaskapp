from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    #app.run(host='::', port=54188)
    #app.run(host='129.148.33.28', port=54188)
    app.run(host='0.0.0.0', port=5000)
