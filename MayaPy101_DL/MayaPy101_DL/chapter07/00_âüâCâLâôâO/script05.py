#def setGengaKeyframe():
#	selection = cmds.ls(sl=True)
#	if not selection:
#		return
#	
#	mel.eval('SetKey')
#	currentTime = cmds.currentTime(q=True)
	for node in selection:
		cmds.keyframe(node, tds=True, t=(currentTime,currentTime))
