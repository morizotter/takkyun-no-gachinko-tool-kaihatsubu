#class Settings(object):
#	中略
	def save(self):
		saveData = {	'across':self.across,
						'merge':self.merge,
						'softEdge':self.softEdge,
						'threshold':self.threshold
						}
		if not os.path.exists(self.__filename):	
			os.makedirs(os.path.dirname(self.__filename))
			
		with open(self.__filename, 'w') as f:
			json.dump(saveData, f)
