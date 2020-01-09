from src.screenshot import Screenshot
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from json import dumps
from urllib.parse import urlparse
import time
import calendar
import os
from src.verifyKey import VerifyKey

app = Flask(__name__)
api = Api(app)

PATH = '/home/jose/Projects/malware-patrol/ScreenShot-API'

class GetScreenshot(Resource):
    def post(self):
        token = request.args.get('token')

        verify = VerifyKey(PATH, token)
        if(verify.isAuthorized()):
            url = request.json['url']
            full = request.json['options']['fullPage']
            formatType = request.json['options']['type']
            quality = request.json['options']['quality']

            netloc = urlparse(url).netloc
            netloc = netloc.replace('.', '_')
            netloc = netloc.replace(':', '_')
            ts = calendar.timegm(time.gmtime())
            filename = '{}_{}'.format(ts, netloc)

            screenshot = Screenshot(PATH, '/src')
            answer = screenshot.getImage(full, filename, url, formatType)

            if(answer == True):
                mimeType = 'image/{}'.format(formatType)
                filename = './temp/screenshots/{}.{}'.format(filename, formatType)
                return send_file(filename, mimetype=mimeType)
            else:
                return {'status':'false'}
        
        else:
            return {'status':'unauthorized'}

api.add_resource(GetScreenshot, '/screenshot')

if __name__ == '__main__':
    app.run()