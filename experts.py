import os
from flask import Flask, request
from flask import jsonify
import Image

from lib.shannon import *
from lib.image_utils import *

app = Flask(__name__)

@app.route('/shannon', methods=['GET', 'POST'])
def shannon():
	imagedata = request.files['imagedata']		
	im = Image.open(imagedata)

	shannon = shannon_entropy(im)
		
	return jsonify(stat="ok", shannon=shannon)	
		
		
@app.route('/shannon/region', methods=['GET', 'POST'])
def shannon_region():		
	imagedata = request.files['imagedata']		
	im = Image.open(imagedata)
	
	shannon_region = sliced_shannon(im)
	return jsonify(stat="ok", shannon_region=shannon_region)
			
	
		