import os
import shutil

def grab_files(folder):
	contents = os.listdir(folder)
	return contents


#folder = str(raw_input("What path do you want to check: "))
folder = r"Y:\Projects\X148\Design\sessions"
folder = folder.replace("\\","\\\\")
print (folder)

in_folder = grab_files(folder)

print (in_folder)

for item in in_folder:
	isfile = item.split(".")
	if len(isfile) == 2:
		if isfile[1] == "sx":
			file_in = open(str(item), "r")
			file_out = open(str(item)+".o", "w")
			netlist = file_in.read()
			file_in.close()
			netlist = netlist.split("\n")
			for line in netlist:
			    new_line = line.replace("X124", "X148")  #first is item to search, #second item to replace
			    new_line = new_line.replace("x124", "x124")
			    file_out.write(new_line+"\n")
			file_out.close()
			shutil.copy(str(item), str(item)+".bak")
			shutil.copy(str(item)+".o", str(item))
			os.remove(str(item)+".o")

