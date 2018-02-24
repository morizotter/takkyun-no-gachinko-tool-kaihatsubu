#class MainWindow(QtGui.QMainWindow):
#	def __init__(self, *args, **kwargs):
#		＜中略＞
#		menuBar = self.menuBar()
#		menu = menuBar.addMenu('File')
#		
#		action  = menu.addAction('Save Settings')
		action.triggered.connect(optionWidget.saveSettings)
#		
#		action  = menu.addAction('Reset Settings')
		action.triggered.connect(optionWidget.resetSettings)
