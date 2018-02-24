#class OptionWidget(QtGui.QWidget):
#	def __init__(self, *args, **kwargs):
#		＜中略＞
#		
#		self.__threshold = QtGui.QDoubleSpinBox(self)
#		self.__threshold.setMinimum(0)
#		self.__threshold.setMaximum(9999)
#		self.__threshold.setDecimals(5)
#		mainLayout.addRow('Threshold', self.__threshold)
#
		self.initialize()
	
	def initialize(self):
		self.__across.button(settings.across).setChecked(True)
		self.__marge.setChecked(settings.merge)
		self.__softEdge.setChecked(settings.softEdge)
		self.__threshold.setValue(settings.threshold)
