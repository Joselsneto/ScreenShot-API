from src.screenshot import Screenshot
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from json import dumps
from urllib.parse import urlparse
from requests.utils import requote_uri
import time
import calendar
import os
from src.checker import Checker
from src.verifyKey import VerifyKey
from src.errors import Errors

app = Flask(__name__)
api = Api(app)

KEYS_PATH = '/home/jose/Projects/malware-patrol/ScreenShot-API'
SCREENSHOT_PATH = '/home/jose/Projects/malware-patrol/ScreenShot-API/temp/screenshots'
FIREFOX_PATH = '/usr/bin/firefox'
TOR_PROFILE = 'TorProxy'

class GetScreenshot(Resource):
    def post(self):
        token = request.args.get('token')
        verify = VerifyKey(KEYS_PATH, token)
        if(verify.isAuthorized()):
            url = request.json['url']
            url = requote_uri(url)
            full = request.json['options']['fullPage']
            formatType = request.json['options']['type']
            quality = request.json['options']['quality']
            tor = request.json['options']['tor']
            timeout = request.json['options']['timeout']

            checker = Checker(url, full, formatType, quality, tor, timeout)
            checkerAnswer = checker.verifyAll()

            if(checkerAnswer != 0):
                return {'error':checkerAnswer.first , 'error-description':checkerAnswer.second}

            netloc = urlparse(url).netloc
            netloc = netloc.replace('.', '_')
            netloc = netloc.replace(':', '_')
            ts = calendar.timegm(time.gmtime())
            filename = 'mps_{}_{}'.format(ts, netloc)

            screenshot = Screenshot(SCREENSHOT_PATH, FIREFOX_PATH)
            answer = screenshot.getImage(full, filename, url, formatType, tor, TOR_PROFILE, timeout)

            if(answer == 0):
                mimeType = 'image/{}'.format(formatType)
                filename = '{}/{}.{}'.format(SCREENSHOT_PATH ,filename, formatType)
                return send_file(filename, mimetype=mimeType)
            else:
                return {'error':answer.first, 'error-description':answer.second}
        
        else:
            return {'error': Errors.UNAUTHORIZED.first, 'error-description': Errors.UNAUTHORIZED.second}

api.add_resource(GetScreenshot, '/screenshot')

if __name__ == '__main__':
    app.run()