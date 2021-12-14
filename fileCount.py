#! /usr/bin/env1 python3
import os
path = "/home/haminton212/Desktop/script/"
count_file = 0
count_dir = 0
for root, dirs, files in os.walk(path):
	for dir1 in dirs:
		count_dir = count_dir + 1
	for file1 in files:
		count_file = count_file + 1
print(f"{count_dir}, {count_file}")
