from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QProgressBar(window)
widget.setRange(0, 100)
widget.setFormat('%p%')
widget.setValue(50)
layout.addWidget(widget)

window.show()
