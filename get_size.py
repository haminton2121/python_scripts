#! /usr/bin/env1 python3
import os
size_dir = 0
size_file = 0
path = "/home/haminton212/Desktop/script"
for root, dirs, files in os.walk(path):
	for dir1 in dirs:
		size_dir = os.path.getsize(dir1) + size_dir
	for file1 in files:
		size_file = os.path.getsize(file1) + size_file
print(f"{size_dir}, {size_file}")