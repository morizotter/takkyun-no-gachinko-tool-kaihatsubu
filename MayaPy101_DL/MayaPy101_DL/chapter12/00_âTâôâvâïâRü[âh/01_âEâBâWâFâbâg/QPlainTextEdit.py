from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QPlainTextEdit(window)
widget.setPlainText('text line 1\ntext line2')
layout.addWidget(widget)

window.show()

print widget.toPlainText()
