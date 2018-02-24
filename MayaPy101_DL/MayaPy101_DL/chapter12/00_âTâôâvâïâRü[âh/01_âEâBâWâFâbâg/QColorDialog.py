from myTool.lib import qt
from PySide import QtGui, QtCore

dialog = QtGui.QColorDialog(qt.getMayaWindow())
result = dialog.exec_()
if result:
	print dialog.selectedColor()