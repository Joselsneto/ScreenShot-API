from .errors import Errors
from .urlValidation import UrlValidation
import httplib2

class Checker:
    
    def __init__(self, url, full, formatType, quality, tor, timeout, browser, height, width):
        self.url = url
        self.full = full
        self.formatType = formatType
        self.quality = quality
        self.tor = tor
        self.timeout = timeout
        self.browser = browser
        self.height = height
        self.width = width

    def verifyUrl(self):
        if(type(self.url) != str):
            return Errors.URL_IS_NOT_STRING

        if(not UrlValidation.url(self.url, False) and not UrlValidation.url(self.url, True)):
            return Errors.MALFORMED_URL

        try:
            h = httplib2.Http()
            resp = h.request(self.url, 'HEAD')
            print(resp[0]['status'])
            if(int(resp[0]['status']) < 400):
                return 0
            else:
                return Errors.httpError('http status {}'.format(resp[0]['status']))
        except httplib2.ServerNotFoundError:
            return Errors.URL_NOT_FOUND
        except Exception as e:
            print(str(e))
            return Errors.exceptionError(str(e))

        return 0

    def verifyFull(self):
        if(type(self.full) != bool):
            return Errors.FULL_IS_NOT_BOOL

        return 0

    def verifyFormatType(self):
        if(type(self.formatType) != str):
            return Errors.FORMAT_TYPE_IS_NOT_STRING
        
        for s in Errors.VALID_FORMAT_TYPES:
            if(s == self.formatType):
                return 0

        return Errors.INVALID_FORMAT_TYPE

    def verifyQuality(self):
        if(type(self.quality) != int):
            return Errors.QUALITY_IS_NOT_INT

        if(self.quality < 0 or self.quality > 100):
            return Errors.QUALITY_OUT_OF_BOUNDS

        return 0

    def verifyTor(self):
        if(type(self.tor) != bool):
            return Errors.TOR_IS_NOT_BOOL

        return 0

    def verifyTimeout(self):
        if(type(self.timeout) != int):
            return Errors.TIMEOUT_IS_NOT_INT
        
        if(self.timeout < 5 or self.timeout > 60):
            return Errors.TIMEOUT_OUT_OF_BOUNDS

        return 0

    def verifyBrowser(self):
        if(self.browser == None):
            return Errors.REQUIRED_BROWSER

        if(type(self.browser) != str):
            return Errors.BROWSER_IS_NOT_STRING
        
        for s in Errors.VALID_BROWSERS:
            if(s == self.browser):
                return 0
        
        return Errors.INVALID_BROWSER

    def verifyHeight(self):
        if(type(self.height) != int):
            return Errors.HEIGHT_IS_NOT_INT
        
        if(self.height < 400):
            return Errors.HEIGHT_OUT_OF_BOUNDS
        
        return 0
    
    def verifyWidth(self):
        if(type(self.width) != int):
            return Errors.WIDTH_IS_NOT_INT

        if(self.width < 400 or self.width > 1920):
            return Errors.WIDTH_OUT_OF_BOUNDS

        return 0

    def verifyAll(self):
        answer = self.verifyUrl()
        if(answer != 0):
            return answer

        answer = self.verifyFull()
        if(answer != 0):
            return answer

        answer = self.verifyFormatType()
        if(answer != 0):
            return answer

        answer = self.verifyQuality()
        if(answer != 0):
            return answer

        answer = self.verifyTor()
        if(answer != 0):
            return answer

        answer = self.verifyTimeout()
        if(answer != 0):
            return answer

        answer = self.verifyBrowser()
        if(answer != 0):
            return answer

        answer = self.verifyHeight()
        if(answer != 0):
            return answer

        answer = self.verifyWidth()
        if(answer != 0):
            return answer
            
        return 0