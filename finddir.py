import os
a = "module_a.py"
for root,dirs,files in os.walk("/home/haminton212/Desktop/package1/"):
	for File in files:
		if a in File:
			print("found")
			break