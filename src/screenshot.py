from subprocess import STDOUT, check_output, TimeoutExpired
import os
from .errors import Errors
from .imageConverter import ImageConverter

TIMEOUT = 15

class Screenshot:

    def __init__(self, screenshotPath, firefoxPath):
        self.screenshotPath = screenshotPath
        self.firefoxPath = firefoxPath

    def createCommand(self, full, fileName, url, tor, torProfile, heigth = '800', width = '600'):
        command = 'timeout {} {} --screenshot {}'.format(TIMEOUT, self.firefoxPath, fileName)
        if(full == False):
            command = '{} --window-size={},{}'.format(command, heigth, width)
        if(tor == True):
            command = '{} -P {}'.format(command, torProfile)
        command = '{} {}'.format(command, url)
        return command

    def getImage(self, full, name, url, fmt, tor, torProfile, heigth = '800', width = '600'):        
        try:
            fileName = os.path.abspath('{}/{}.png'.format(self.screenshotPath, name))
            command = self.createCommand(full, fileName, url, tor, torProfile, heigth, width)
            output = check_output(command, stderr=STDOUT, shell=True, timeout=TIMEOUT)
            newFile = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, fmt))
            ImageConverter.convert(fileName, fmt, newFile)
            return 0
        except TimeoutExpired:
            return Errors.TIMEOUT_EXPIRED
        except Exception as e:
            print(str(e))
            return Errors.exceptionError(str(e))    