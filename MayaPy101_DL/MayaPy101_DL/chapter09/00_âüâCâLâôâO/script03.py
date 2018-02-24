class OptionWidget(QtGui.QWidget):
	def __init__(self, *args, **kwargs):
		super(OptionWidget, self).__init__(*args, **kwargs)
		
		layout = QtGui.QGridLayout(self)
		
		stockerView = StockerView(self)
		layout.addWidget(stockerView, 0, 0, 1, 2)
		
		button = QtGui.QPushButton('Copy', self)
		layout.addWidget(button, 1, 0)
		
		button = QtGui.QPushButton('Paste', self)
		layout.addWidget(button, 1, 1)
