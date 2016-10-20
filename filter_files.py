#!/usr/bin/env python

import os
import sys
import shutil

#find the extension .tex in all files within the myforlder directory
def find_extension():
	path = os.walk('/myforlder/')
	extension = '.tex' 
	for root, dirs, files in path:
		for documento in files:
			if extension in documento:
					yield (os.path.join(root, documento))


# copy the filtered files in a folder called "folder_one"					
def copy_files():
	for x in find_extension():
		archivo = os.path.split(x)
		folders = os.path.dirname(x)
		destination = '/folder_one/' + folders
		todo = destination
		if not os.path.exists(destination):
			shutil.copytree(folders, destination)
		elif os.path.exists(destination):
			shutil.copy(x, destination)
		else:
			continue
			
copy_files();
