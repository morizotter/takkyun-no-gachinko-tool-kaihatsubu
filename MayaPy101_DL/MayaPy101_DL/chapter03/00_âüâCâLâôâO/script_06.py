shapes = cmds.listRelatives(selection[0], s=True, pa=True, type='mesh')
if not shapes:
	cmds.error('Node has no shape.')