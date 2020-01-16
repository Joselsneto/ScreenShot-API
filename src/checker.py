from .errors import Errors
from .urlValidation import UrlValidation
import httplib2

class Checker:
    
    def __init__(self, url, full, formatType, quality, tor):
        self.url = url
        self.full = full
        self.formatType = formatType
        self.quality = quality
        self.tor = tor

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

        return 0