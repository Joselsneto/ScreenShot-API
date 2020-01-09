from subprocess import STDOUT, check_output
import os

TIMEOUT = 15

class Screenshot:

    def __init__(self, path, fit):
        self.path = os.path.abspath('{}/{}'.format(path, fit))

    def getImage(self, full, name, url, fmt, heigth = '800', width = '600'):
        if(full == True):
            localScript = '{}/firefoxScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            try:
                command = 'timeout ' + str(TIMEOUT) + ' firefox --screenshot ' + fileName + ' ' + url
                os.system(command)
                return True
            except:
                return False
        else:
            localScript = '{}/chromeScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            try:
                command = 'timeout ' + str(TIMEOUT) + ' firefox --screenshot ' + fileName + ' --window-size=' + str(heigth) + ',' + str(width) + ' ' + url 
                os.system(command)
                return True
            except:
                return False