import re

#Define the input file here
file_in = open("input.ckt", "r")

#define the output file here
file_out = open("output.ckt", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:
	match_mos = re.search("^xm", line)
	match_resist = re.search("^xr", line)
	match_bip = re.search("^xq", line)
	if match_mos:
		line = line.replace(" n ", " nsvtlp ")
		line = line.replace(" p ", " psvtlp ")
		line = line.replace(" pht ", " phvtlp ")
		line = line.replace(" nht ", " nhvtlp ")
	elif match_resist:
                line = line.replace(" rppolywo ", " rpporpo ")
	elif match_bip:
                line = line.replace(" pnp", " pnps25")
	file_out.write(line+"\n")
file_out.close()
