#	def paste(self):
#		indexes = self.__getIndexes()
#		for index in indexes:
#			～中略～
#			(node, attr, value) = self.__model.rowData(index.row())
			
			nodes = cmds.ls(sl=True)
			for node in nodes:
				if not cmds.attributeQuery(attr, n=node, ex=True):
					OpenMaya.MGlobal.displayError(
						'%s has not %s.' % (node, attr)
						)
					continue
