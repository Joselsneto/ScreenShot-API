import subprocess
import os

class Screenshot:

    def __init__(self, fit):
        self.path = '{}/{}'.format(os.getcwd(), fit)

    def getImage(self, full, name, url, fmt, heigth = '800', width = '600'):
        if(full == True):
            localScript = '{}/firefoxScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            subprocess.call([localScript, fileName, url])
        else:
            localScript = '{}/chromeScreenshot.sh'.format(self.path)
            fileName = os.path.abspath('{}/../temp/screenshots/{}.{}'.format(self.path, name, fmt))
            subprocess.call([localScript, fileName, heigth, width, url])