
#Define the input file here
file_in = open("input.cir", "r")

#define the output file here
file_out = open("output.ckt", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:
    line = line.split(" ")
    if line[0]!= "":    #prevents script from crashing when nothing in line
        if line[0][0] == "m":
            line[0]="x"+line[0]
    line = " ".join(line)
    file_out.write(line+"\n")

file_out.close()
