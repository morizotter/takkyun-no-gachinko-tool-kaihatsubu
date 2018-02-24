class ToolWidget(QtGui.QWidget):
	applied = QtCore.Signal()
	closed = QtCore.Signal()

	def __init__(self, *args, **kwargs):
		super(ToolWidget, self).__init__(*args, **kwargs)
