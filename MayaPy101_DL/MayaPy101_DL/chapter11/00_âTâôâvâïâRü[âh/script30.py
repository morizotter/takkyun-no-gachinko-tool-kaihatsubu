from maya import cmds
selection = cmds.ls(sl=True)
for dst in selection:
	nodeType = cmds.objectType(dst)
	if nodeType != 'transform':
		continue
	cmds.rename(dst, 'transform_#')
