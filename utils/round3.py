import math

def roundToThirdPowerOf10(num):
	suffixes = ['', 'k', 'M', 'B', 'T']
	logarithm = math.floor(math.log(num, 1000))
	roundedNumber = math.floor(num / (1000 ** logarithm))
	return (str(roundedNumber) + suffixes[logarithm])