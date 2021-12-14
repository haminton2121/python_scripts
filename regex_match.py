#! /usr/bin/env1 python3
import re
import os
path = "/home/haminton212/Desktop/script"
for root, dirs, files in os.walk(path):
	for file1 in files:
		b = re.match(r"\w+\.\w+",file1)
		if b:
			print("dung roi")

