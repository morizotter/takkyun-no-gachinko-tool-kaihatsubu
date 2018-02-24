#def main():
#	filename = cmds.fileDialog2(
#					ds=2, cap='Save Image', fm=0, ff='*.bmp'
#					)
#	if not filename:
#		return
	result = save(filename[0])
	if result:
		OpenMaya.MGlobal.displayInfo('Done!')
	else:
		OpenMaya.MGlobal.displayError('Failed to save picture.')
