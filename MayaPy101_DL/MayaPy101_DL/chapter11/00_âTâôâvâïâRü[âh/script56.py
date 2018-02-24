class Point(Float3):
	def distanceTo(self, point):
		x = (self.x() - point.x())**2
		y = (self.y() - point.y())**2
		z = (self.z() - point.z())**2
		return math.sqrt(x + y + z)
