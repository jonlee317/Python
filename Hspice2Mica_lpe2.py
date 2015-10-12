#############################################################
# In this conversion file we lower case all the characters  #
#            and                                            #
# we also add x in front of the M of all transistors        #
#                                                           #
#############################################################

import os

#Define the input file here
file_in = open("input.netlist", "r")

#define the output file here
file_out = open("output.netlist", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
#print (netlist)
netlist = netlist.split("\n")
#print (netlist)

#iteration for line by line
for line in netlist:
    new_line = line.lower()
    new_line2 = new_line.replace("'","")

    #new_line3 = new_line2.split(" ")
    #if new_line3[0]!= "":    #prevents script from crashing
    #	if new_line3[0][0] == "m" or new_line3[0][0] == "q":
    #		new_line3[0]="x"+new_line3[0]
    #new_line4 = " ".join(new_line3)

    file_out.write(new_line2+"\n")

file_out.close()
os.remove('input.netlist')
