from subprocess import STDOUT, check_output, TimeoutExpired
import os
from .errors import Errors
from .imageConverter import ImageConverter

TIMEOUT = 15

class Screenshot:

    def __init__(self, screenshotPath, firefoxPath):
        self.screenshotPath = screenshotPath
        self.firefoxPath = firefoxPath

    def getImage(self, full, name, url, fmt, heigth = '800', width = '600'):
        if(full == True):
            fileName = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, 'png'))
            try:
                command = 'timeout {} {} --screenshot {} {}'.format(TIMEOUT, self.firefoxPath, fileName, url)
                output = check_output(command, stderr=STDOUT, shell=True, timeout=TIMEOUT)
                newFile = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, fmt))
                ImageConverter.convert(fileName, fmt, newFile)
                return 0
            except TimeoutExpired:
                return Errors.TIMEOUT_EXPIRED
            except Exception as e:
                print(str(e))
                return Errors.exceptionError(str(e))
        else:
            fileName = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, 'png'))
            try:
                # command = 'timeout ' + str(TIMEOUT) + ' firefox --screenshot ' + fileName + ' --window-size=' + str(heigth) + ',' + str(width) + ' ' + url 
                command = 'timeout {} {} --screenshot {} --window-size={},{} {}'.format(TIMEOUT, self.firefoxPath, fileName, heigth, width, url)
                output = check_output(command, stderr=STDOUT, shell=True, timeout=TIMEOUT)
                newFile = os.path.abspath('{}/{}.{}'.format(self.screenshotPath, name, fmt))
                ImageConverter.convert(fileName, fmt, newFile)
                return 0
            except TimeoutExpired:
                return Errors.TIMEOUT_EXPIRED
            except Exception as e:
                print(str(e))
                return Errors.exceptionError(str(e))