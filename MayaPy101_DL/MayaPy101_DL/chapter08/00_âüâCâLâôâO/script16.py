#class OptionWidget(QtGui.QWidget):
#	def __init__(self, *args, **kwargs):
#		super(OptionWidget, self).__init__(*args, **kwargs)
#		mainLayout = QtGui.QFormLayout(self)
#
#		xy = QtGui.QRadioButton('XY', self)
#		yz = QtGui.QRadioButton('YZ', self)
#		xz = QtGui.QRadioButton('XZ', self)
#
		acrossLayout = QtGui.QHBoxLayout(self)
		acrossLayout.addWidget(xy, True)
		acrossLayout.addWidget(yz, True)
		acrossLayout.addWidget(xz, True)
