# This script converts bits 
# from register 1 into bits of two and places them into reg 1 and reg 2
# from register 2 into bits of two and places them into reg 3 and reg 4
# from register 3 into bits of two and places them into reg 1 and reg 2
# from register 4 into bits of two and places them into reg 3 and reg 4

#Define the input file here
file_in = open("output.v", "r")

#define the output file here
file_out = open("output2.v", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")



#iteration for line by line
my_list = []
for line in netlist:

    line = line.split("=")
    if line[0] != "":    #prevents script from crashing when nothing in line
    	if len(line[0]) > 1:
	        if line[0][0] == "8" or line[0][1] == "8":
	            if line[1][0] != "2":
	            	my_list.append(line)
	            	print my_list

my_list = sorted(my_list)
file_out.write(my_list)
    #file_out.write("10'b%s" % first_full)
    #file_out.write("10'b%s" % second_full)

file_out.close()
