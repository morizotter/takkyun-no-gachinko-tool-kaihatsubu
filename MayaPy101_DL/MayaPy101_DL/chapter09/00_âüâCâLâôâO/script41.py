#	def pasteFromClipboard(self):
#		clipboard = QtGui.QApplication.clipboard()
#		mimeData  = clipboard.mimeData()
#		if not mimeData.hasFormat(StockerView.mimeType):
#			return
		datas = mimeData.data(StockerView.mimeType)
		datas = json.loads(str(datas))
