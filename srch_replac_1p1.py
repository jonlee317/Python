
#Define the input file here
file_in = open("test.cir", "r")

#define the output file here
file_out = open("output.txt", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:

    new_line = line.replace(" P ", " PLT ")  #first is item to search, #second item to replace
    new_line = new_line.replace(" VDD ", " VDDX ")  #first is item to search, #second item to replace
    
    file_out.write(new_line+"\n")

file_out.close()
