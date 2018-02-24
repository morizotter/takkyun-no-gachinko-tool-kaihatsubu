# -*- coding: utf-8 -*-
from maya import OpenMayaUI, cmds
from PySide import QtGui
import shiboken

def getMayaWindow():
	ptr = OpenMayaUI.MQtUtil.mainWindow()
	widget = shiboken.wrapInstance(long(ptr), QtGui.QWidget)
	return widget
