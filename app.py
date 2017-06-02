from flask import Flask
import pydevd

app = Flask(__name__)

@app.route('/')
def hello_world():
    #pydevd.settrace('203.117.132.170', port=5000, stdoutToServer=True, stderrToServer=True)
    print "inside hello world route"
    return 'Hello World!'


if __name__ == '__main__':
    pydevd.settrace('203.117.132.170', port=5000, stdoutToServer=True, stderrToServer=True)
    #app.run(host='0.0.0.0', port=5000)
    app.run()
