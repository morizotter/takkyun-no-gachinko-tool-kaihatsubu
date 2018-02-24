import os
from maya import cmds

path = cmds.workspace(q=True, rd=True)
path = os.path.normpath(path)
os.popen('explorer \"' + path + '\"')