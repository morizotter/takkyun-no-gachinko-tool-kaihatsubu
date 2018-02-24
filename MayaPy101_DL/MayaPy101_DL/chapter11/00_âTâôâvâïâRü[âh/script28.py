from maya import cmds
selection = cmds.ls(sl=True)
for i, dst in enumerate(selection):
	cmds.rename(dst, 'node_'+str(i))	# ループ回数を文字列に変換してリネームに使う
