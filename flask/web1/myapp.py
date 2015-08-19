from flask import Flask

fapp = Flask(__name__)

from app import modules, routes

import sys

print('myapp.path:%s' % sys.path)
