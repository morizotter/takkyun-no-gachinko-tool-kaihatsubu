from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QDial(window)
widget.setRange(0, 32)
widget.setValue(16)
widget.setNotchesVisible(True)
layout.addWidget(widget)

window.show()
