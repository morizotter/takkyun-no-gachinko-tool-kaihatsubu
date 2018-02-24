from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QSpinBox(window)
widget.setRange(-100, 100)
widget.setValue(64)
layout.addWidget(widget)

window.show()