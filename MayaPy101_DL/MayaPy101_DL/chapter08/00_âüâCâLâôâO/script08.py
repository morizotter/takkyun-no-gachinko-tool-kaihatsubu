#	if softEdge: 
#		vertices       = cmds.polyListComponentConversion(
#							shape,
#							fv=1, ff=1, fe=1, fuv=1, fvf=1, tv=1
#							)
#		vertices       = cmds.ls(vertices, fl=True)
		
		centerVertices = []
		for vertex in vertices:
			pos = cmds.pointPosition(vertex, w=True)
			if abs(pivot[index] - pos[index]) <= threshold:
				centerVertices.append(vertex)
