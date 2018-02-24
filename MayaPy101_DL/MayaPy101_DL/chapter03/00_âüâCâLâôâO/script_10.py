for dst in selection[1:]:
	shapes = cmds.listRelatives(dst, s=True, pa=True, type='mesh')
	if not shapes:
		continue

	dstSkinCluster = cmds.listConnections(	shapes[0]+'.inMesh',
											s=True,
											d=False
											)