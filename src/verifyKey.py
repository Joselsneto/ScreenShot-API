import mmap
import os

class VerifyKey:

    def __init__(self, key):
        self.key = key
        self.path = os.path.abspath('{}/{}'.format(os.getcwd(), 'authorized_keys'))
    
    def isAuthorized(self):
        try:
            fp = open(self.path)
            line = fp.readline()
            while line:
                if(line.strip() == self.key):
                    return True
                line = fp.readline()
        except:
            return False
        finally:
            fp.close()
        return False