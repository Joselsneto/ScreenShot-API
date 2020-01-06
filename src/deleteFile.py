import os
from threading import Thread
import time

class DeleteFile(Thread):

    def __init__(self, path):
        Thread.__init__(self)
        self.path = path
    
    def run(self):
        time.sleep(15)
        if os.path.exists(self.path):
            os.remove(self.path)