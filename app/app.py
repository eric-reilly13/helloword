from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "I love you so much baby"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)