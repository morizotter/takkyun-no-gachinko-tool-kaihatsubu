#class MainWindow(QtGui.QMainWindow):
#	def __init__(self, *args, **kwargs):
#		super(MainWindow, self).__init__(*args, **kwargs)
#		self.setWindowTitle('Mirror Geometry')
#		self.resize(400, 200)
#
#		toolWidget = qt.ToolWidget(self)
#		self.setCentralWidget(toolWidget)
#
#		optionWidget = OptionWidget(self)
#		toolWidget.setOptionWidget(optionWidget)
#
		toolWidget.setActionName(self.windowTitle())
		toolWidget.applied.connect(qt.Callback(optionWidget.apply))
		toolWidget.closed.connect(self.close)
