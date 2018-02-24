from maya import cmds
selected = cmds.ls(sl=True)
for node in selected:
	nodeType = cmds.objectType(node)
	if nodeType != 'transform':
		break
	cmds.rename(node, 'transform_#')
