from myTool.lib import qt
from PySide import QtGui, QtCore

result = QtGui.QMessageBox.warning(
			qt.getMayaWindow(),
			'Scene Not Saved',
			'Save changes to untitled scene?',
			(QtGui.QMessageBox.Save|
			QtGui.QMessageBox.Discard|
			QtGui.QMessageBox.Cancel),
			QtGui.QMessageBox.Save)