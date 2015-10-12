import os
import shutil
import re

#Define the input file here
file_in = open("input.cir", "r")

#define the output file here
file_out = open("output.cir", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
#print (netlist)
netlist = netlist.split("\n")
#print (netlist)

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
os.remove('input.cir')