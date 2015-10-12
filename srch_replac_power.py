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
	line = line.replace("vdd ", "vdda ")
	line = line.replace("vss ", "vssa ")
	match_subckt = re.search("subckt", line)
	match_gate = re.search("^xg", line)
	match_inst = re.search("^xi", line)
	match_gate1 = re.search("^x1i", line)
	match_gate2 = re.search("^x2i", line)
	match_gate3 = re.search("^x3i", line)
	match_resist = re.search("^xr", line)
	match_insto = re.search("^xo", line)
	match_rppolywo = re.search("rppolywo", line)
	match_cp1p2 = re.search("cp1p2", line)
	match_cpolppw = re.search("cpolppw", line)

	if 	match_subckt:
		new_line = line.split(" ")
		new_line.insert(2, "vssa")
		new_line.insert(2, "vdda")
		new_line = " ".join(new_line)
	elif match_resist:
		new_line = line.split(" ")
		if len(new_line) == 4:
			new_line.insert(1, "vssa")
			new_line.insert(1, "vdda")
		new_line = " ".join(new_line)
	elif match_gate or match_inst or match_gate1 or match_gate2 or match_gate3 or match_insto:
		new_line = line.split(" ")
		if not(match_rppolywo) and not(match_cp1p2) and not(match_cpolppw):
			new_line.insert(1, "vssa")
			new_line.insert(1, "vdda")
		new_line = " ".join(new_line)
	else:
		new_line = line.split(" ")
		new_line = " ".join(new_line)

	file_out.write(new_line+"\n")
file_out.close()
