#	def copyToClipboard(self):
		data    = []
		indexes = self.selectionModel().selectedIndexes()
		if not indexes:
			return
