for dst in selection[1:]:
	shapes = cmds.listRelatives(dst, s=True, pa=True, type='mesh')
	if not shapes:
		continue

	dstSkinCluster = cmds.listConnections(	shapes[0]+'.inMesh',
											s=True,
											d=False
											)
	# ここから追加									
	if not dstSkinCluster:
		dstSkinCluster = cmds.skinCluster(
							dst,
							influences,
							omi=maintainMaxInfluences,
							mi=maxInfluences,
							dr=dropoffRate,
							sm=skinningMethod,
							nw=normalizeWeights,
							tsb=True,
							)
	dstSkinCluster = dstSkinCluster[0]