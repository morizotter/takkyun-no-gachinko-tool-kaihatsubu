#class StockItemModel(QtGui.QStandardItemModel):
#	～略～
	def rowData(self, index):
		node  = self.item(index, 0).text()
		attr  = self.item(index, 1).text()
		value = self.item(index, 2).data()
		
		return (node, attr, value)
