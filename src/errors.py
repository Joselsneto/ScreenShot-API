from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"])

class Errors:

    VALID_FORMAT_TYPES = ['jpeg', 'png', 'jpg']
    VALID_BROWSERS = ['google-chrome', 'firefox']

    URL_IS_NOT_STRING           = Pair(-100, "The url must be a string")
    MALFORMED_URL               = Pair(-101, "Invalid url")
    URL_NOT_FOUND               = Pair(-102, "Url not found")
    FULL_IS_NOT_BOOL            = Pair(-103, "Full must be a bool")
    FORMAT_TYPE_IS_NOT_STRING   = Pair(-104, "Format type must be a string")
    INVALID_FORMAT_TYPE         = Pair(-105, "Format type must be one of the following: " + ', '.join(VALID_FORMAT_TYPES))
    QUALITY_IS_NOT_INT          = Pair(-106, "Quality must be an int")
    QUALITY_OUT_OF_BOUNDS       = Pair(-107, "Quality value must be between 0 and 100")
    TOR_IS_NOT_BOOL             = Pair(-108, "Tor must be a bool")
    TIMEOUT_IS_NOT_INT          = Pair(-109, "Timeout must be an int")
    TIMEOUT_OUT_OF_BOUNDS       = Pair(-110, "Timeout value must be between 5 and 60")
    BROWSER_IS_NOT_STRING       = Pair(-111, "Browser must be a string")
    INVALID_BROWSER             = Pair(-112, "Browser must be one of the following: " + ','.join(VALID_BROWSERS))
    HEIGHT_IS_NOT_INT           = Pair(-113, "Height must be an int")
    HEIGHT_OUT_OF_BOUNDS        = Pair(-114, "Height value must be more or equal 400")
    WIDTH_IS_NOT_INT            = Pair(-115, "Width must be an int")
    WIDTH_OUT_OF_BOUNDS         = Pair(-116, "Width must be between 400 and 1920")

    REQUIRED_BROWSER            = Pair(-200, "Browser is a required field")
    REQUIRED_URL                = Pair(-201, "URL is a required field")
    REQUIRED_FULL               = Pair(-202, "Full is a required field")
    REQUIRED_FORMAT_TYPE        = Pair(-203, "Format type is a required field")
    REQUIRED_TIMEOUT            = Pair(-204, "Timeout is a required field")    

    TIMEOUT_EXPIRED             = Pair(-300, "Timeout expired")

    UNKNOWN_ERROR               = Pair(-400, "Unknown error, please create an issue with the request in https://github.com/Joselsneto/ScreenShot-API/issues")

    UNAUTHORIZED                = Pair(-500, "Unauthorized")

    def exceptionError(e):
        return Pair(-301, e)

    def httpError(e):
        return Pair(-500, e)