from PySide import QtCore
from myTool.modeling import mirrorGeometry
reload(mirrorGeometry) 

widget = mirrorGeometry.OptionWidget()
widget.setWindowFlags(QtCore.Qt.Window)	# Windowモードに変更
widget.show()
