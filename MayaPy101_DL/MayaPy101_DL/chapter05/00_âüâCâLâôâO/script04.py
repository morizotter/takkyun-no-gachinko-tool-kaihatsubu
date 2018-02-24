# -*- coding: utf-8 -*-
from maya import cmds

def main():
	samplerInfoList = cmds.ls(type='samplerInfo')
	if not samplerInfoList:
		samplerInfo = cmds.shadingNode('samplerInfo', asUtility=True)
	else:
		samplerInfo = samplerInfoList[0]
