from myTool.lib import qt
from PySide import QtGui, QtCore

dialog = QtGui.QMessageBox(qt.getMayaWindow())
dialog.setText('Infomation!')
result = dialog.exec_()
