
import os,sys,re


path = "."

if __name__ == "__main__" :

	if len(sys.argv) == 2:
		path = sys.argv[1]


	reg1 = "print[.*' '(]"
	reg2 = "import pdb"

	for path, subdirs, files in os.walk(path):
		for name in files:
			if name.endswith(".py"):
				fn = os.path.join(path, name)
				line_num = 1
				with open(fn) as myf:
					prt = re.compile(reg1)
					pb = re.compile(reg2)
					for line in myf:
						line = line.lstrip(' ')
						if not line.startswith("#"):
							if prt.findall(line):
								print("\x1b[1;32;40m{0:4d} :: {1:2s} --> {2}\x1b[0m".format(line_num,fn,prt.findall(line)))
							if pb.findall(line):
								print("\x1b[1;31;40m{0:4d} :: {1:2s} --> {2}\x1b[0m".format(line_num,fn,pb.findall(line)))
						line_num+=1
				#print (os.path.join(path, name))

		
		
		
		
		
		
		
		
		
		
		
		
	
	