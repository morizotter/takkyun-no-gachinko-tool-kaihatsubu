class Float3(object):
	def __init__(self, x, y, z):
		self.__x = x
		self.__y = y
		self.__z = z
		
	def x(self):
		return self.__x
	
	def setX(self, value):
		self.__x = float(value)
	
	def y(self):
		return self.__y
	
	def setY(self, value):
		self.__y = float(value)
	
	def z(self):
		return self.__z
	
	def setZ(self, value):
		self.__z = float(value)
	
	def __add__(self, vector):
		if isinstance(vector, Float3):
			x = self.__x + vector.x()
			y = self.__y + vector.y()
			z = self.__z + vector.z()
		
		elif type(vector) == list or type(vector) == tuple:
			x = self.__x + vector[0]
			y = self.__y + vector[1]
			z = self.__z + vector[2]
		
		else:
			x = self.__x + vector
			y = self.__y + vector
			z = self.__z + vector
	
	@classmethod
	def fromList(cls, data):
		return cls(float(data[0]), float(data[1]), float(data[2]))
		
class Vector(Float3):		
	def length(self):
		return math.sqrt(self.x()**2 + self.y()**2 + self.z()**2)
