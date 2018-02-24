class Vector(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def length(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)
	
	def __add__(self, vec):
		return Vector(self.x+vec.x, self.y+vec.y, self.z+vec.z)
