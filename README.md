panel of experts
---

A small set of image processing routines, wrapped up in a httpony.

Set up
---

There are a few dependencies to look out for. You can either install them manually, or use the commands below.

This can be installed locally on your system pretty easily using [virtualenv](https://pypi.python.org/pypi/virtualenv) and [pip](http://www.pip-installer.org/).

Just clone this repository and do the following commands:

    $ cd panel-of-experts ( or wherever you cloned it to )
    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install -r requirements.txt

You can then run the server locally using [foreman](http://theforeman.org/) like this:

    $ foreman start

If you want to skip all that and you already have the dependencies installed on your system, just do:

    $ gunicorn experts:app


Dependencies
---

* [Flask](http://flask.pocoo.org/)
* [PIL](http://www.pythonware.com/products/pil/)
* [gunicorn](http://gunicorn.org/)

Use
---

Presently there is only one expert in the house and his name is [Claude Shannon](http://en.wikipedia.org/wiki/Claude_Shannon). He was an information theory expert, and his "Shannon Entropy" algorithm is available in two ways.

Shannon Entropy
---

The first is the Shannon Entropy value for a given image. To use this, with your server running ( I'm using foreman on http://0.0.0.0:5000 ), do the following command:

    $ curl -F imagedata=@/path/to/your/file.jpg http://0.0.0.0:5000/shannon

If all goes well, this should return some data as json like what you see here:

    {
	  "shannon": 8.031213510557613, 
	  "stat": "ok"
	}
	
Regional Shannon Entropy
---

This routine uses the same Shannon Entropy algorithm, but splits the image into blocks and then returns the highest Shannon Entropy for a region within the image. We though this might be a useful way to search for the most interesting "part" of an image.

To use, simply perform the following command:

    $ curl -F imagedata=@/path/to/your/file.jpg http://0.0.0.0:5000/shannon/region

This should result in some similar json data:

    { 
	  "shannon_region": {
	    "shannon": 8.705446926336688, 
	    "x": 500, 
	    "y": 100
	  }, 
	  "stat": "ok"
	}
	
The difference being that you now see an x and y coordinate value. This represents the top left corner of the region in the image with the highest Shannon Entropy where the origin ( 0,0 ) is the top left corner of the image. Currently the size of the box we are using is fixed at 100x100 pixels.

On the web
---

I've also added a tool to let you play with this in your web browser. This lets load an image from the web and display the region with the highest Shannon Entropy in your browser. To use, just go to your web browser and enter a URL like the following.

    http://0.0.0.0:5000/shannon/region/web?url=http://somewebsite.com/someimage.jpg

And if you'd like to try it right now, it's up on [Heroku](http://panel-of-experts.herokuapp.com/shannon/region/web?url=http://images.collection.cooperhewitt.org/44047_34b5838a8cd2a176_b.jpg)

Random Regions
---

There is a fairly dumb method called random_region. This simply returns some JSON in a similar format to the other experts on the panel to indicate a "random" spot in an image. I say it's dumb, because it's just finding a random pixel in the image and anyone could easily do that. But, I wanted to continue with the notion of an "API" and I do sort of consider random to be one of the experts.

To use it, just like the rest:

    $ curl -F imagedata=@/path/to/your/file.jpg http://0.0.0.0:5000/random/region

And get back some JSON like:

    {
	  "random_region": {
	    "x": 3287, 
	    "y": 1946
	  }, 
	  "stat": "ok"
	}
