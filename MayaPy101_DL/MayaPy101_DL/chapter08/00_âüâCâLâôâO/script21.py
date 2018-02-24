#		self.__softEdge = QtGui.QCheckBox('Soft Edge', self)
#		mainLayout.addRow('', self.__softEdge)
#
		self.__threshold = QtGui.QDoubleSpinBox(self)
		self.__threshold.setMinimum(0)
		self.__threshold.setMaximum(9999)
		self.__threshold.setDecimals(5)
		mainLayout.addRow('Threshold', self.__threshold)
