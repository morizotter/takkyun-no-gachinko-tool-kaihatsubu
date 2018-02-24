class MainWindow(QtGui.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Mirror Geometry')
		self.resize(400, 200)
