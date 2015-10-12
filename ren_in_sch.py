import os
import shutil
import re

def grab_files(folder):
	contents = os.listdir(folder)
	return contents

# Enter your folder path here:
folder = r"Y:\Projects\X148\Design\sch"

folder = folder.replace("\\","\\\\")
print (folder)

in_folder = grab_files(folder)

print (in_folder)

for item in in_folder:
	isfile = item.split(".")
	if len(isfile) == 2:
		if isfile[1] == "1" or isfile[1] == "2" or isfile[1] == "3" or isfile[1] == "4":
			file_in = open(str(item), "r")
			file_out = open(str(item)+".o", "w")
			netlist = file_in.read()
			file_in.close()
			netlist = netlist.split("\n")
			for line in netlist:
			    new_line = line.replace("X124:X124", "X148:X148")  #first is item to search, #second item to replace
			    new_line = new_line.replace("3 X124", "3 X148")
			    new_line = new_line.replace("PROJECT=X124", "PROJECT=X148")
			    new_line = new_line.replace("@NAME=X124", "@NAME=X148")
			    new_line = new_line.replace("NWV = 0.17", "NWV = 0.2")
			    if re.match("T 869 44 10 0 3", new_line):
			    	strip_line = new_line[:15]
			    	new_line = strip_line+" MXU 2014-08-05"
			    file_out.write(new_line+"\n")
			file_out.close()
			shutil.copy(str(item), str(item)+".bak")
			shutil.copy(str(item)+".o", str(item))
			os.remove(str(item)+".o")