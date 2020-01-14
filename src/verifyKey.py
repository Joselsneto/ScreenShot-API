import mmap
import os

class VerifyKey:

    def __init__(self, path, key):
        self.key = key
        self.path = os.path.abspath('{}/{}'.format(path, 'authorized_keys'))
    
    def isAuthorized(self):
        fp = None
        try:
            fp = open(self.path)
            line = fp.readline()
            while line:
                if(line.strip().split()[0] == self.key):
                    return True
                line = fp.readline()
        except:
            return False
        finally:
            fp.close()
        return False