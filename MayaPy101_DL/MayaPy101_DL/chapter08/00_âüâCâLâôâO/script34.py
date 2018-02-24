from PySide import QtCore
from myTool.lib import qt
reload(qt)

widget = qt. ToolWidget ()
widget.setWindowFlags(QtCore.Qt.Window)	# Windowモードに変更
widget.show()
