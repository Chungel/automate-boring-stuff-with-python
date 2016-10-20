#!/usr/bin/env python

import os
import sys
import shutil

def delete_files():
	if os.path.exists('/folder_one/'):
		shutil.rmtree('/folder_one/')
	else:
		return False	

delete_files()

