from maya import cmds
def main(baseName, start=0):
	selectionNodes = cmds.ls(sl=True)
	for node in selectionNodes:
		try:
			cmds.rename(node, baseName+str(start))
			start += 1
		except:
			print node+u'は、リネームできませんでした'
