from maya import cmds
selection = cmds.ls(sl=True)

i = 0
while i<len(selection):
	cmds.rename(selection[i], 'node_'+str(i))
	i = i+1	# 繰り返した数を記憶する
			# コレを忘れると、無限ループになります。
