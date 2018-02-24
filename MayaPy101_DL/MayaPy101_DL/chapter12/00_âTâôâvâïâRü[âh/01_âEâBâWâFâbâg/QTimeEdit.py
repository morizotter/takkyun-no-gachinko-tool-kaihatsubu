from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QTimeEdit(window)
time = QtCore.QTime(23,59,0)
widget.setTime(time)
layout.addWidget(widget)

window.show()
