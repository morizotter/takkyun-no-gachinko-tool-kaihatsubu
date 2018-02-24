#	def appendItem(self, nodename, attrname, value):
#		～中略～
#		valueItem = QtGui.QStandardItem(str(value))	
#		valueItem.setEditable(False)
#		valueItem.setData(type(value))
		
		self.appendRow([nodeItem, attrItem, valueItem])
