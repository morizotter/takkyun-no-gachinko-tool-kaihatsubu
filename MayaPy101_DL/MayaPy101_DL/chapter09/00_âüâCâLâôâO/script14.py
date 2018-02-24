#	def copy(self):
#		self.__model.removeRows(0, self.__model.rowCount())
#		
#		cb = mel.eval('$temp=$gChannelBoxName;')
#		nodeList = cmds.channelBox(cb, q=True, mol=True)
#		attrList = cmds.channelBox(cb, q=True, sma=True)
		self.__setItems(nodeList, attrList)
		
		nodeList = cmds.channelBox(cb, q=True, sol=True)
		attrList = cmds.channelBox(cb, q=True, ssa=True)
		self.__setItems(nodeList, attrList)
		
		nodeList = cmds.channelBox(cb, q=True, hol=True),
		attrList = cmds.channelBox(cb, q=True, sha=True)
		self.__setItems(nodeList, attrList)
