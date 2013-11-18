import Image, math
import Levenshtein

# Set of tools for comparing images

# Calculate Mean Squared Error
#def mse(image_a, image_b):
	
#	tmp = sum((a-b)**2 for a, b in zip(image_a, image_b))
#	mse = float(tmp) / self.x / self.y
	
#	return mse
	
# Calculate Peak Signal to Noise Ratio
#def psnr(image_a, image_b):

	# psnr = 20 * math.log(self._pixel / math.sqrt(self.mse), 10)
	
# Calculate Normalized Root Mean Square Deviation
#def nrmsd(image_a, image_b):
	# self._nrmsd = math.sqrt(self.mse) / self._pixel
	
# Calculate Levenshtein distance
#def Levenshtein(image_a, image_b):
	
	#stra = ''.join((chr(x) for x in self.imga_int))
	#strb = ''.join((chr(x) for x in self.imgb_int))

	#lv = Levenshtein.distance(stra, strb)

	#self._lv = float(lv) / self.x / self.y