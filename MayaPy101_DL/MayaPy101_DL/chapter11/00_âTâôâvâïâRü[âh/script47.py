import math
class Vector(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def length(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)
