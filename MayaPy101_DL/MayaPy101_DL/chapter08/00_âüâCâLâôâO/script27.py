#class ToolWidget(QtGui.QWidget):
#	applied = QtCore.Signal()
#	closed  = QtCore.Signal()
#
#	def __init__(self, *args, **kwargs):
#		super(ToolWidget, self).__init__(*args, **kwargs)
#		mainLayout = QtGui.QGridLayout(self)
#		self.setLayout(mainLayout)
#
		self.__scrollWidget = QtGui.QScrollArea(self)
		self.__scrollWidget.setWidgetResizable(True)
		self.__scrollWidget.setFocusPolicy(QtCore.Qt.NoFocus)
		self.__scrollWidget.setMinimumHeight(1)
		mainLayout.addWidget(self.__scrollWidget, 0, 0, 1, 3)
