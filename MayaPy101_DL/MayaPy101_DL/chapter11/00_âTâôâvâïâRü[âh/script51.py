class Vector(object):
	def __init__(self, x, y, z):
		self.__x = x				# 変数名の前に「__」を追加して
		self.__y = y				# 外部から変更しにくいようにする
		self.__z = z
	
	def x(self):					# Xの値を教えてあげるメソッド
		return self.__x
	
	def setX(self, value):			# Xの値を設定するメソッド
		self.__x = float(value)
	
	def y(self):					# Yの値を教えてあげるメソッド
		return self.__y
	
	def setY(self, value):			# Yの値を設定するメソッド
		self.__y = float(value)
	
	def z(self):					# Zの値を教えてあげるメソッド
		return self.__z
	
	def setZ(self, value):			# Zの値を設定するメソッド
		self.__z = float(value)
		
	def length(self):
		return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)
	
	def __add__(self, vec):
		return Vector(	self.__x + vec.x(),
						self.__y + vec.y(),
						self.__z + vec.z()
						)
# 使用例
vecA = Vector(0, 1, 0)
vecB = Vector(1, 0, 0)
vecC = vecA + vecB
print vecC.x(), vecC.y(), vecC.z()
