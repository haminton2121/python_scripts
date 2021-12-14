#! /usr/bin/env1 python3
import os
path = "/home/haminton212/Desktop/script/"
for i in range(10):
	os.rmdir(f"{path}{i}-folder")
