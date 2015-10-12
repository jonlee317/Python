import os
import shutil
import re

def grab_files(folder):
	contents = os.listdir(folder)
	return contents


#folder = str(raw_input("What path do you want to check: "))
folder = r"Y:\Projects\X165\Design\x165bgr\x165bgr_up_test\mtc\test"
folder = folder.replace("\\","\\\\")
print (folder)

in_folder = grab_files(folder)

print (in_folder)

for item in in_folder:
	isfile = item.split(".")
	if len(isfile) == 2:
		if isfile[1] == "cir":
			file_in = open(str(item), "r")
			file_out = open(str(item)+".o", "w")
			netlist = file_in.read()
			file_in.close()
			netlist = netlist.split("\n")
			for line in netlist:
				#file_out.write(new_line+"\n")
				match_mos = re.search("^M", line)	
				match_nm = re.search("NM", line)
				match_pm = re.search("PM", line)		
				if match_mos and not match_nm and not match_pm:
					elements = line.split(" ")
					first_element = elements[0]
					m_fact = elements[8].split("=")
					num_fing = int(m_fact[1])
					count = 0
					while (count < num_fing):
						elements[0] = elements[0]+"_"+str(count)
						elements.pop()
						elements.append("M=1")
						line = " ".join(elements)
						file_out.write(line+"\n")
						elements[0] = first_element
						count += 1
				else:
					file_out.write(line+"\n")
			file_out.close()
			shutil.copy(str(item), str(item)+".bak")
			shutil.copy(str(item)+".o", str(item))
			os.remove(str(item)+".o")

