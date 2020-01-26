from subprocess import STDOUT, check_output, TimeoutExpired
import os
from .errors import Errors
from .imageConverter import ImageConverter

# TIMEOUT = 15

class Screenshot:

    def __init__(self, screenshotPath, firefoxPath, chromePath, torProfile):
        self.screenshotPath = screenshotPath
        self.firefoxPath = firefoxPath
        self.chromePath = chromePath
        self.torProfile = torProfile

    def createCommand(self, full, fileName, url, tor, timeout, browser, height = '600', width = '800'):
        if(browser == 'firefox'):
            command = 'timeout {} {} --screenshot {}'.format(timeout, self.firefoxPath, fileName)
            if(full == False):
                command = '{} --window-size={},{}'.format(command, width, height)
            if(tor == True):
                command = '{} -P {}'.format(command, self.torProfile)
            command = '{} {}'.format(command, url)
            return command
        elif(browser == 'google-chrome'):
            # TODO verify if exist a away that chrome can get screenshot of the entire site
            # TODO verify how I can set TOR profile on chrome
            command = 'timeout {} google-chrome --headless --disable-gpu --screenshot={} --window-size={},{} --default-background-color=0 {}'.format(timeout, fileName, width, height, url)
            return command

    def getImage(self, full, name, url, fmt, tor, timeout, browser, height = '600', width = '800'):        
        try:
            fileName = os.path.abspath('{}/{}.png'.format(self.screenshotPath, name))
            command = self.createCommand(full, fileName, url, tor, timeout, browser, height, width)
            output = check_output(command, stderr=STDOUT, shell=True, timeout=timeout)
            newFile = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, fmt))
            ImageConverter.convert(fileName, fmt, newFile)
            return 0
        except TimeoutExpired:
            return Errors.TIMEOUT_EXPIRED
        except Exception as e:
            print(str(e))
            return Errors.exceptionError(str(e))    