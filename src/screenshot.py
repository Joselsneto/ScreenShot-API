import subprocess
import os

class Screenshot:

    def __init__(self, fit):
        print(fit)
        self.path = '{}{}'.format(os.getcwd(), fit)
        print(self.path)
        print(fit)

    def getImage(self, full, name, url, format, heigth = 800, width = 600):
        if(full == True):
            localScript = self.path + '/firefoxSreenshot.sh'
            subprocess.call([localScript, name, format, url])
        else:
            localScript = self.path + '/chromeScreenshot.sh'
            subprocess.call([localScript, name, format, heigth, width, url])


screenshot = Screenshot('')
screenshot.getImage(True, 'google', 'https://google.com', 'png')