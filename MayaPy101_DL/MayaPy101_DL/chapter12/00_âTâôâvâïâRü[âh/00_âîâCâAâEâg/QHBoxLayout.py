from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)

layout = QtGui.QHBoxLayout(window)
layout.addWidget(QtGui.QPushButton('Button A'))
layout.addWidget(QtGui.QPushButton('Button B'))
layout.addWidget(QtGui.QPushButton('Button C'))
window.show()