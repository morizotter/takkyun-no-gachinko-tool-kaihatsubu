#	def removeSelectedItem(self):
#		model	 = self.model()
#		selModel = self.selectionModel()
		
		while selModel.selectedIndexes():
			indexes = selModel.selectedIndexes()
			model.removeRow(indexes[0].row())
