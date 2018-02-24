from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QFrame(window)
widget.setFrameShape(QtGui.QFrame.HLine)
widget.setFrameShadow(QtGui.QFrame.Sunken)
layout.addWidget(widget)

window.show()
