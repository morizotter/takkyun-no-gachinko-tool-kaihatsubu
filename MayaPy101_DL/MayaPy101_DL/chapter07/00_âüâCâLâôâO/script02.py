def setDougaKeyframe():
	selection = cmds.ls(sl=True)
	if not selection:
		return
	mel.eval('SetKey')
