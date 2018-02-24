# -*- coding: utf-8 -*-
from maya import cmds

def main():
	samplerInfoList = cmds.ls(type='samplerInfo')
	if not samplerInfoList:
		samplerInfo = cmds.shadingNode('samplerInfo', asUtility=True)
	else:
		samplerInfo = samplerInfoList[0]
		
	ramp = cmds.shadingNode('ramp', n='fresnel_ramp', asTexture=True)
	cmds.removeMultiInstance(ramp+'.colorEntryList[2]', b=True)
	cmds.setAttr(ramp+'.colorEntryList[0].color', 1, 1, 1) 	# 1つ目のポイントの色
	cmds.setAttr(ramp+'.colorEntryList[0].position', 0)	#1つ目のポイントの位置
	cmds.setAttr(ramp+'.colorEntryList[1].color', 0, 0, 0)	#2つ目のポイントの色
	cmds.setAttr(ramp+'.colorEntryList[1].position', 0.6)	#2つ目のポイントの位置
	cmds.connectAttr(samplerInfo+'.facingRatio', ramp+'.vCoord')
	