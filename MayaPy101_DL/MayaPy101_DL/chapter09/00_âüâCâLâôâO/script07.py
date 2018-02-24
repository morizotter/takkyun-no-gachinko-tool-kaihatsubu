#class OptionWidget(QtGui.QWidget):
#	def __init__(self, *args, **kwargs):
#		～略～
#		stockerView = StockerView(self)
#		layout.addWidget(stockerView, 0, 0, 1, 2)
		
		self.__model = StockItemModel(self)
		stockerView.setModel(self.__model)
		
		self.__selModel = QtGui.QItemSelectionModel(self.__model)
		stockerView.setSelectionModel(self.__selModel)
		
#		button = QtGui.QPushButton('Copy', self) 
#		～略～
