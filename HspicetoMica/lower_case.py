
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

#iteration for line by line
for line in netlist:
    new_line = line.lower()
    new_line2 = new_line.replace("'","")
    
    file_out.write(new_line2+"\n")
    #file_out.write(new_line)

file_out.close()
