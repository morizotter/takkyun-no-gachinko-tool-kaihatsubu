#「Transform」を処理の対象とする
transforms = cmds.ls(type='transform')

#「lambert」を処理の対象とする
lamberts = cmds.ls(type='lambert')

#「アニメーションカーブ」を処理の対象とする
animCurves = cmds.ls(type=['animCurveTU','animCurveTA','animCurveTL'])

#「ドリブンのアニメーションカーブ」を処理の対象とする
drivenAnimCurves = cmds.ls(type=['animCurveUU','animCurveUA','animCurveUL'])

#「DAGノード」を処理の対象とする
dagNodes = cmds.ls(dag=True)

#「マテリアル」を処理の対象とする
#厳密には、HyperShadeの「Materials」のタブにあるもの
materials = cmds.ls(mat=True)

#「テクスチャ」を処理の対象とする
#厳密には、HyperShadeの「Textures」のタブにあるもの
textures = cmds.ls(textures=True)

#「すべてのノード」を処理の対象とする
nodes = cmds.ls(allPaths=True)

#「Transform」を処理の対象とする
#cmds.ls(type='transform')と同等
transforms = cmds.ls(transforms=True)

#「ライト」を処理の対象とする
lights = cmds.ls(lights=True)

#「カメラ」を処理の対象とする
cameras = cmds.ls(cameras=True)
