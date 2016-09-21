#############################################################
#
# In this conversion file 
# 1)  lowercase all character
# 2)  Remove the ' character
#                                                           
#############################################################

import os

#Define the input file here
file_in = open("input.mcnet", "r")

#define the output file here
file_out = open("output.mcnet", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:
    new_line = line.lower()
    new_line2 = new_line.replace("'","")

    file_out.write(new_line2+"\n")

file_out.close()
os.remove('input.mcnet')
