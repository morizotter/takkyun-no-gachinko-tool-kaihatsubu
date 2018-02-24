class Vector(object):
	# ～中略～
	def __add__(self, vector):
		# Vector + Vectorの場合
		if isinstance(vector, Vector):
			x = self.__x + vector.x() 	
			y = self.__y + vector.y() 
			z = self.__z + vector.z() 	
		
		# Vector + list か Vector + tupleの場合
		elif type(vector) == list or type(vector) == tuple:
			x = self.__x + vector[0] 
			y = self.__y + vector[1] 
			z = self.__z + vector[2] 
		
		# それ以外の場合
		else:
			x = self.__x + vector
			y = self.__y + vector 
			z = self.__z + vector 
			
		return Vector(x, y, z) 

vecA = Vector(0, 1, 0)
vecB = Vector(1, 0, 0)
vecC = vecA + vecB
print vecC.x(), vecC.y(), vecC.z()

vecD = vecA + [0, 0, 1]
print vecD.x(), vecD.y(), vecD.z()

vecE = vecA + 1
print vecE.x(), vecE.y(), vecE.z()
