#class MainWindow(QtGui.QMainWindow):
#	def __init__(self, *args, **kwargs):
#中略
#		toolWidget.setActionName(self.windowTitle())
#		toolWidget.applied.connect(qt.Callback(optionWidget.apply))
#		toolWidget.closed.connect(self.close)
#
#		menuBar = self.menuBar()
#		menu = menuBar.addMenu('File')
		action  = menu.addAction('Save Settings')
		action  = menu.addAction('Reset Settings')
