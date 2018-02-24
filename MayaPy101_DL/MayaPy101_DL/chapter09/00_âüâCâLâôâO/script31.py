#	def paste(self):
#		indexes = self.__getIndexes()
#		for index in indexes:
#			～中略～
#			for node in nodes:
#				～中略～

				try:
					cmds.setAttr('%s.%s' % (node,attr), value)
				
				except:
					OpenMaya.MGlobal.displayError(
						'%s.%s : Failed to set value.' % (node,attr)
						)
