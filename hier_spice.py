import re

#define the input file here
file_in = open("input.cir", "r")

#define the output file here
file_out = open("output.spi", "w")

#reading the input file
netlist = file_in.read()
file_in.close()


#converting the netlist to line by line format
netlist = netlist.split("\n")

#iteration for line by line
for line in netlist:
        line = line.replace("/ ", "")
        line = line.replace(" P ", " PFET ")
        line = line.replace(" N ", " NFET ")
        line = line.replace(" PH ", " EGPFET ")
        line = line.replace(" NH ", " EGNFET ")
        #replacing the numbers
        line = line.replace("='PWV'", "=0.08u")
        line = line.replace("='NWV'", "=0.08u")
        line = line.replace("='PLV'", "=0.03u")
        line = line.replace("='NLV'", "=0.03u")
        line = line.replace("='PLHV'", "=0.27u")
        line = line.replace("='NLHV'", "=0.27u")
        line = line.replace("='PWHV'", "=0.36u")
        line = line.replace("='NWHV'", "=0.36u")        
        line = line.replace("=PWV", "=0.08u")
        line = line.replace("=NWV", "=0.08u")
        line = line.replace("=PLV", "=0.03u")
        line = line.replace("=NLV", "=0.03u")
        line = line.replace("=PLHV", "=0.27u")
        line = line.replace("=NLHV", "=0.27u")
        line = line.replace("=PWHV", "=0.36u")
        line = line.replace("=NWHV", "=0.36u")        
        line = line.replace("*NWV", "*0.08u")
        line = line.replace("*NWHV", "*0.36u")  
        line = line.replace("R_PN", "2.9")
        line = line.replace("VPNP", "VPNP W=3.2e-06 L=3.2e-06")

        match_egnfet = re.search("egnfet", line, flags=re.IGNORECASE)
        match_egpfet = re.search("egpfet", line, flags=re.IGNORECASE)
        match_nfet = re.search("nfet", line, flags=re.IGNORECASE)
        match_pfet = re.search("pfet", line, flags=re.IGNORECASE)

        if match_egnfet or match_egpfet or match_nfet or match_pfet:
        	line_split = line.split(" ")
        	line_split.append("p_la=0")
        	line = " ".join(line_split)

        match_opreres = re.search("opreres", line, flags=re.IGNORECASE)

        if match_opreres:
        	line_split = line.split(" ")
        	line_split.append("pbar=1 s=1")
        	tmp_value = line_split.pop(3)
        	line_split.insert(4, "$SUB="+tmp_value)
        	line = " ".join(line_split)

        match_mult1 = re.search("mult=1", line, flags=re.IGNORECASE)

        if match_mult1:
        	line_split = line.split(" ")
        	line_split.pop()
        	line_split.append("spacefinger_mx=1e-07 wfinger_mx=1e-07 fr_big_finger=0")
        	line = " ".join(line_split)

        file_out.write(line+"\n")

#Adding mom subckt
file_out.write("\n.SUBCKT CMOM_6U1X_2T8X_LB_2P minus plus\n")
file_out.write(".ENDS\n\n")

file_out.close()

def add_u(input):
        input = str(input)
        input = input+"u"
        return input
