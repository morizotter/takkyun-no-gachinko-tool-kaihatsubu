class Vector(object):
	# ～中略～
	@classmethod
	def fromList(cls, data):
		return cls(float(data[0]), float(data[1]), float(data[2]))

		