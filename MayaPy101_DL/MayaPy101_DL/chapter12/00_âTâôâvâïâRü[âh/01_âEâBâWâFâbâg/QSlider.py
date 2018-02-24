from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QSlider(QtCore.Qt.Horizontal,window)
widget.setRange(0, 32)
widget.setValue(16)
layout.addWidget(widget)

window.show()
