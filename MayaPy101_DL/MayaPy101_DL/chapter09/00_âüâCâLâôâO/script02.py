class MainWindow(QtGui.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Copy Attribute')
		self.resize(430, 260)
		
		optionWidget = OptionWidget(self)
		self.setCentralWidget(optionWidget)
