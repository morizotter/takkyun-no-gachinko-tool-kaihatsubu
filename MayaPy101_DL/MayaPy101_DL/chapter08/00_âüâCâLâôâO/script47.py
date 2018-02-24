#class Settings(object):
#	def __init__(self):
#		temp = __name__.split('.')
#		self.__filename = os.path.join(
#							os.getenv('MAYA_APP_DIR'),
#							temp[0],
#							temp[-1]+'.json'
#							)
		self.reset()

	def reset(self):
		self.across     = 1
		self.merge      = True
		self.softEdge   = True
		self.threshold  = 0.001
