#class StockerView(QtGui.QTreeView):
#	mimeType = 'application/x-mytool-copyattribute-data'
#	～中略～
#	def copyToClipboard(self):
#		～中略～
#		mimeData = QtCore.QMimeData()
#		mimeData.setData(
#			StockerView.mimeType,
#			QtCore.QByteArray(json.dumps(data))
#		)
		clipboard = QtGui.QApplication.clipboard()
		clipboard.setMimeData(mimeData)
