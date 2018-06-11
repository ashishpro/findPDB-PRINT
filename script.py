'''import os,sys

import pdb
file_list = []
for path, subdirs, files in os.walk("D:"):
	for name in files:
		f = os.path.join(path, name)
		file_list.extend(f)
		
print(file_list)
print("length: {}".format(len(file_list)))
'''

import os
import re
f = []

reg1 = "print[.*' '(]"
reg2 = "import pdb"
import pdb
for path, subdirs, files in os.walk("."):
	for name in files:
		if name.endswith(".py"):
			fn = os.path.join(path, name)
			line_num = 1
			with open(fn) as myf:
				prt = re.compile(reg1)
				pb = re.compile(reg2)
				for line in myf:
					if prt.findall(line):
						print("\x1b[1;32;40m{0:4d} :: {1:2s} --> {2}\x1b[0m".format(line_num,fn,prt.findall(line)))
					if pb.findall(line):
						print("\x1b[1;31;40m{0:4d} :: {1:2s} --> {2}\x1b[0m".format(line_num,fn,pb.findall(line)))
					line_num+=1
			f.append(fn)
			#print (os.path.join(path, name))

		
for x in f:
	print(x,end='\n')
	
'''
with open("./sample.txt") as myf:
	line_num = 1
	prt = re.compile(reg1)
	pb = re.compile(reg2)
	for line in myf:
		if prt.findall(line):
			print("\x1b[1;32;40m{0} :: {1} --> {2}\x1b[0m".format(line_num,os.path.join(".","sample.txt"),prt.findall(line)))
		if pb.findall(line):
			print("\x1b[1;31;40m{0} :: {1} --> {2}\x1b[0m".format(line_num,os.path.join(".","sample.txt"),pb.findall(line)))
		line_num+=1
		'''

		
		
		
		
		
		
		
		
		
		
		
		
	
	