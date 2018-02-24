# -*- coding: utf-8 -*-
from maya import cmds

def main():
	samplerInfo = cmds.shadingNode('samplerInfo', asUtility=True)