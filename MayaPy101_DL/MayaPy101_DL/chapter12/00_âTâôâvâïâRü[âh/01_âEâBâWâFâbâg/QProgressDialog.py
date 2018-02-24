import time
from myTool.lib import qt
from PySide import QtGui, QtCore

dialog = QtGui.QProgressDialog(
			'Upload files...',
			'Cancel',
			0,
			100,
			qt.getMayaWindow(),
			QtCore.Qt.WindowModal
			)
dialog.show()

for i in range(100):
	# キャンセルのボタンが押せるおまじない
	QtGui.QApplication.processEvents()
	
	# キャンセルされている場合は、終了
	if dialog.wasCanceled():
		break
		
	dialog.setValue(i)
	
	# サンプルの為、0.1秒待機する
	time.sleep(0.1)

dialog.close()