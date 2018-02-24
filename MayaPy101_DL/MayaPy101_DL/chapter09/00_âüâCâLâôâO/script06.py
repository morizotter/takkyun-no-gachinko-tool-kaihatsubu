#class StockItemModel(QtGui.QStandardItemModel):
#	def __init__(self, parent=None):
#		super(StockItemModel, self).__init__(0, 3, parent)
		self.setHeaderData(0, QtCore.Qt.Horizontal, 'Node')
		self.setHeaderData(1, QtCore.Qt.Horizontal, 'Attribute')
		self.setHeaderData(2, QtCore.Qt.Horizontal, 'Value')
