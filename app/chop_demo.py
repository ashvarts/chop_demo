import logging
import subprocess
from flask import Flask
VERSION = '2.0.0'
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/version')
def version():
    result = subprocess.Popen(['/usr/bin/env python', '--version'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    return result.stdout.read()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting Up CHOP Demo ...')
    app.run(host='0.0.0.0', port='5000')
