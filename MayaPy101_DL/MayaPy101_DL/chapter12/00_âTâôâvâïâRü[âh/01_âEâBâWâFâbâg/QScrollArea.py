from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QScrollArea(window)
widget.setWidgetResizable(True)
layout.addWidget(widget)

image = QtGui.QLabel()
image.setPixmap(QtGui.QPixmap(r'C:\Program Files\Autodesk\Maya2016\icons\MayaStartupImage.png'))
widget.setWidget(image)
window.show()
