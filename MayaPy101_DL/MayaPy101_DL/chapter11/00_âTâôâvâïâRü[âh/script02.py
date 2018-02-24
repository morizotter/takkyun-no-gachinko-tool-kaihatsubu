from maya import cmds
sphere = cmds.polySphere()
radius = cmds.polySphere(sphere[1], q=True, r=True)
radius = radius * 10
cmds.polySphere(sphere[1], e=True, r=radius)
