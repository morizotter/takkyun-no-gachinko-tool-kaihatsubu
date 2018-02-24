#class OptionWidget(QtGui.QWidget):
#中略
	def saveSettings(self):
		settings.across = self.__across.checkedId()
		settings.merge = self.__marge.isChecked()
		settings.softEdge = self.__softEdge.isChecked()
		settings.threshold = self.__threshold.value()
		settings.save()

