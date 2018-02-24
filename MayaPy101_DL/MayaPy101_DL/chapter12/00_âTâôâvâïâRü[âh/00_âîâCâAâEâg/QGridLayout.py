from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)

layout = QtGui.QGridLayout(window)
layout.addWidget(QtGui.QPushButton('Button A'), 0, 0)
layout.addWidget(QtGui.QPushButton('Button B'), 0, 1)
layout.addWidget(QtGui.QPushButton('Button C'), 0, 2)
layout.addWidget(QtGui.QPushButton('Button D'), 1, 0, 1, 3)
window.show()