srcSkinCluster = srcSkinCluster[0]
skinningMethod = cmds.getAttr(srcSkinCluster+'.skm')
dropoffRate = cmds.getAttr(srcSkinCluster+'.dr')
maintainMaxInfluences = cmds.getAttr(srcSkinCluster+'.mmi')
maxInfluences = cmds.getAttr(srcSkinCluster+'.mi')
bindMethod = cmds.getAttr(srcSkinCluster+'.bm')
normalizeWeights = cmds.getAttr(srcSkinCluster+'.nw')
influences = cmds.skinCluster(srcSkinCluster, q=True, inf=True)