import logging
import platform
from flask import Flask
VERSION = '2.0.0'
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/version')
def version():
    return "Python Version: %s \n" % platform.python_version()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting Up CHOP Demo ...')
    app.run(host='0.0.0.0', port='5000')
