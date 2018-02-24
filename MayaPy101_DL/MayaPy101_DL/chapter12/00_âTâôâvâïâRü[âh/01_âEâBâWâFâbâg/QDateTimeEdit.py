from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QDateTimeEdit(window)
date = QtCore.QDate(2016,1,1)
time = QtCore.QTime(20,00,00)
dateTime = QtCore.QDateTime(date, time)
widget.setDateTime(dateTime)
layout.addWidget(widget)

window.show()
