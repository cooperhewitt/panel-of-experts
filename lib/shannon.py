import Image, math

def shannon_entropy(img):

	# calculate the shannon entropy for an image

	histogram = img.histogram()
	histogram_length = sum(histogram)

	samples_probability = [float(h) / histogram_length for h in histogram]

	return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

def sliced_shannon(img):
	
	# calculate the shannon entropy for small slices of an image
	
	w = img.size[0]
	h = img.size[1]
	dims = [ w,h ]

	slice_size = 100
	
	tiles = []
	max_shannon = 0
	
	for y in range(0,h,slice_size):
		for x in range(0,w,slice_size):
			mx = min(x+slice_size, w)
			my = min(y+slice_size, h)
			
			buff = Image.new("RGB", [slice_size, slice_size], (255, 255, 255)) 
			tile = img.crop((x, y, mx, my))
			buff.paste(tile, (0, 0))
		
			shannon = shannon_entropy(buff)
			
			data = {'shannon':shannon, 'x':x, 'y':y}
			if shannon > max_shannon:
				max_shannon = shannon
				tiles = data
	
	return tiles