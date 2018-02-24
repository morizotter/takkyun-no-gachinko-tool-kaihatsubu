from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QSplitter(window)
widget.addWidget(QtGui.QListView())
widget.addWidget(QtGui.QListView())
layout.addWidget(widget)

window.show()
