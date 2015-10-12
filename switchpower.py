import re

#Define the input file here
file_in = open("input.ckt", "r")

#define the output file here
file_out = open("output4.ckt", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:
	line = line.replace(" vdd ", " vdda ")
	line = line.replace(" vss ", " vssa ")
	line = line.replace(" pnp ", " pnps25 ")
	line = line.replace(" pht ", " phvtlp ")
	line = line.replace(" nht ", " nhvtlp ")
	line = line.replace(" rppolywo ", " rpporpo ")
	line = line.replace(" rnpolywo ", " rnporpo ")
	line = line.replace(" p ", " psvtlp ")
	line = line.replace(" n ", " nsvtlp ")


	file_out.write(line+"\n")
file_out.close()
