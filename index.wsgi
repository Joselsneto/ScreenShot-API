#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/jose/Project/malware-patrol/ScreenShot-API/')
from index import app as application
application.secret_key = 'test'
