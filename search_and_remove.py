#!/usr/bin/env python

import os
import sys
import shutil


#search for a string within a directory and remove all files containing that string
def remove_drafts():
	path = os.walk('/folder_one/')
	texto = 'draft'
	extension = '.tex'
	for root, dirs, files in path:
		for documento in files:
			if extension in documento:
				if texto in open(os.path.join(root, documento)).read():
					shutil.rmtree(root)
				else:
					continue
			else:
				continue
	
remove_drafts()

