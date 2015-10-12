#############################################################
# In this conversion file we lower case all the characters  #
#            and                                            #
# we also add x in front of the M of all transistors        #
#                                                           #
#############################################################

import os
import re

#Define the input file here
file_in = open("input2.cir", "r")

#define the output file here
file_out = open("output2.ckt", "w")
file_out2 = open("output3.ckt", "w")

#reading the input file
netlist = file_in.read()
netlist2 = netlist
file_in.close()

#converting the netlist to line by line format
#print (netlist)
netlist = netlist.split("\n")
#print (netlist)

netlist2 = netlist2.split("\n\n")
for block in netlist2:
	match_vdd = re.search("vdd", block)
	match_vss = re.search("vss", block)
	match_vdda = re.search("vdda", block)
	match_vssa = re.search("vssa", block)
	lines = block.split("\n")

	if match_vdd and match_vss:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vss")
				newline.insert(2, "vdd")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vdda and match_vssa:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vssa")
				newline.insert(2, "vdda")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vdda:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vdda")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vssa:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vssa")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vss:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vss")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vdd:
		for line in lines:
			match_subckt = re.search("subckt", line)
			if 	match_subckt:
				newline = line.split(" ")
				newline.insert(2, "vdd")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
			else:
				newline = line.split(" ")
				newline4 = " ".join(newline)
				file_out.write(newline4+"\n")
	else:
		for line in lines:
			newline = line.split(" ")
			newline4 = " ".join(newline)
			file_out.write(newline4+"\n")

	if match_vss:
		print ("vss is present")
	print ("that's it for this block\n")


#iteration for line by line
#for line in netlist:
#    new_line = line.lower()
#    new_line2 = new_line.replace("'","")

#    new_line3 = new_line2.split(" ")
 #   if new_line3[0]!= "":    #prevents script from crashing
#    	if new_line3[0][0] == "m" or new_line3[0][0] == "q":
 #   		new_line3[0]="x"+new_line3[0]
#    new_line4 = " ".join(new_line3)

    #new_line5 = new_line4.split(" ")
    #if new_line5[0]!= "":    #prevents script from crashing
    	#if new_line5[0][0] == "q":
    		#new_line5[0]="x"+new_line5[0]
    #new_line6 = " ".join(new_line5)

#    file_out.write(new_line4+"\n")

file_out.close()
#os.remove('input.cir')
