import os
from flask import Flask, request
from flask import jsonify
import Image

from lib.shannon import *
from lib.image_utils import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def experts():
		# upload and store the image in memory
		imagedata = request.files['imagedata']		
		im = Image.open(imagedata)

		# choose the method/expert
		expert = request.form['expert']
		
		if expert == "shannon":
			shannon = shannon_entropy(im)
			
		return jsonify(stat="ok", expert=expert, shannon=shannon)