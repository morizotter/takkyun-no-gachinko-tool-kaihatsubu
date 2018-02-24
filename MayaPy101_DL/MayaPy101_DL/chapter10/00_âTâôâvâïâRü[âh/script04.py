#「geometry_GP」にある「子のノード」を処理の対象とする
children = cmds.listRelatives('geometry_GP', children=True)

#listRelativesは、同名ノードがある場合処理がエラーしやすくなるので
#fullPathを併用することをオススメします。
children = cmds.listRelatives('geometry_GP', children=True, fullPath=True)

#「joint_GP」にある「子のジョイント」を処理の対象とする
joints = children = cmds.listRelatives(
			'joint_GP',
			children=True,
			fullPath=True,
			type='joint'
			)

#子、孫など末端まで取得したい場合は、「allDescendents」を併用する
joints = children = cmds.listRelatives(
			'joint_GP',
			children=True,
			fullPath=True,
			type='joint',
			allDescendents=True
			)
