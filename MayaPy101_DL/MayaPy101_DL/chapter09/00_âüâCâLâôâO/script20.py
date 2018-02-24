#class StockItemModel(QtGui.QStandardItemModel):
#	～略～
#	def appendItem(self, nodename, attrname, value):
#		nodeItem = QtGui.QStandardItem(nodename)
#		nodeItem.setEditable(False)
#		
#		try:
#			attrname = cmds.attributeName('%s.%s' % (nodename, attrname), l=True)
#		except:
#			pass
#		
#		attrItem = QtGui.QStandardItem(attrname)
#		attrItem.setEditable(False)

		valueItem = QtGui.QStandardItem(str(value))	
		valueItem.setEditable(False)
		valueItem.setData(value)
