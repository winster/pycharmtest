from flask import Flask
import pydevd

app = Flask(__name__)

pydevd.settrace('203.117.132.170', port=5000, stdoutToServer=True, stderrToServer=True)

@app.route('/')
def hello_world():
    print "inside hello world route"
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
