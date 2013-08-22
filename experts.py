import os
from flask import Flask

from lib.shannon import *
from lib.image_utils import *

app = Flask(__name__)

@app.route('/')
def experts():
    return 'Hello Experts!'