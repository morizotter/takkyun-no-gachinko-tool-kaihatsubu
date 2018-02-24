#class Settings(object):
#	def __init__(self):
		temp = __name__.split('.')
		self.__filename = os.path.join(
					os.getenv('MAYA_APP_DIR'),
					temp[0],
					temp[-1]+'.json'
					)
