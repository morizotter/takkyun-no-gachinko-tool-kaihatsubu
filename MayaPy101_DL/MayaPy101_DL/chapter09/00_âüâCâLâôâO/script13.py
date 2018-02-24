#	def copy(self):
#		～略～
#		cb = mel.eval('$temp=$gChannelBoxName;')
		nodeList = cmds.channelBox(cb, q=True, mol=True)
		attrList = cmds.channelBox(cb, q=True, sma=True) 
