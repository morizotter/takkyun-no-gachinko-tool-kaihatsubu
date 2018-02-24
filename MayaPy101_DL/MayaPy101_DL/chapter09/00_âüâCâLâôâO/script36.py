#	def copyToClipboard(self):
#		data    = []
#		indexes = self.selectionModel().selectedIndexes()
#		if not indexes:
#			return
		
		for index in indexes:
			if index.column() != 0:
				continue
			
			data.append(self.model().rowData(index.row()))
