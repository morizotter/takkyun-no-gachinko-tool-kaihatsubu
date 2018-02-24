#class Settings(object):
#	def __init__(self):
#		temp = __name__.split('.')
#		self.__filename = os.path.join(
#							os.getenv('MAYA_APP_DIR'),
#							temp[0],
#							temp[-1]+'.json'
#							)
#		self.reset()
		self.read()
	
	def read(self):
		if os.path.exists(self.__filename):
			with open(self.__filename, 'r') as f:
				saveData = json.load(f)
				self.across    = saveData['across']
				self.merge     = saveData['merge']
				self.softEdge  = saveData['softEdge']
				self.threshold = saveData['threshold']
