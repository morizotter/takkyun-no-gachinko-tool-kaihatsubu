class StockItemModel(QtGui.QStandardItemModel):
	def __init__(self, parent=None):
		super(StockItemModel, self).__init__(0, 3, parent)
