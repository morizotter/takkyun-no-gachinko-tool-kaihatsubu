class Vector(object):
	# ～中略～
	@staticmethod
	def fromList(data):
		return Vector(float(data[0]), float(data[1]), float(data[2]))

listVector = [0, 1, 0]
vecA = Vector.fromList(listVector)
print vecA.x(), vecA.y(), vecA.z()

vecB = vecA.fromList([1,1,1])
print vecB.x(), vecB.y(), vecB.z()
