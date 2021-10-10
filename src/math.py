def GCF(*args):
	x = args[0]
	
	for y in args[1:]:
		while y > 0:
			x, y = y, x % y
	
	return x
	
def LCM(*args):
	x = args[0]
	
	for y in args[1:]:
		x = int(x*y//GCF(x,y))
	
	return x
