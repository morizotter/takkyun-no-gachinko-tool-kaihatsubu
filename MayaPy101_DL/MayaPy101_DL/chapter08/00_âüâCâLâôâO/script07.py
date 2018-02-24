#	cmds.polyMirrorFace(shape, ws=True, d=direction, p=pivot[0:3], **kwargs)

	if softEdge: 
		vertices       = cmds.polyListComponentConversion(
							shape,
							fv=1, ff=1, fe=1, fuv=1, fvf=1, tv=1
							)
		vertices       = cmds.ls(vertices, fl=True)
