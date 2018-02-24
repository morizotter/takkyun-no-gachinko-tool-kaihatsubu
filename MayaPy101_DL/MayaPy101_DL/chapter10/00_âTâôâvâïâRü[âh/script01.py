# 例）ballという名前で、大きさ2のSphereを作成する
from maya import cmds
cmds.polySphere(n='ball', radius=2)

# 例）ballの大きさを調べる
from maya import cmds
print cmds.polySphere('ball', q=True, radius=True)

# 例）ballの大きさを10に変更する
from maya import cmds
cmds.polySphere('ball', e=True, radius=10)
