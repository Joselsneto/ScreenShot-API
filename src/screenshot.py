from subprocess import STDOUT, check_output
import os

TIMEOUT = 15

class Screenshot:

    def __init__(self, fit):
        self.path = os.path.abspath('{}/{}'.format(os.getcwd(), fit))

    def getImage(self, full, name, url, fmt, heigth = '800', width = '600'):
        if(full == True):
            localScript = '{}/firefoxScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            try:
                output = check_output([localScript, fileName, url, str(TIMEOUT)], stderr=STDOUT, timeout=TIMEOUT)
                return True
            except:
                return False
        else:
            localScript = '{}/chromeScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            try:
                output = check_output([localScript, fileName, heigth, width, url, str(TIMEOUT)], stderr=STDOUT, timeout=TIMEOUT)
                return True
            except:
                return False