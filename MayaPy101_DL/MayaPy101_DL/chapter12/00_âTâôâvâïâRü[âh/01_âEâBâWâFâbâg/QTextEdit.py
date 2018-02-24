from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QTextEdit(window)
widget.setHtml('<font color="red">text line1</font><br /><strong>text line2</strong>')
layout.addWidget(widget)

window.show()
