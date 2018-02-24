from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QCalendarWidget(window)
widget.setSelectedDate(QtCore.QDate(2016,1,1))
layout.addWidget(widget)

window.show()
