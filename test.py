# This script converts bits 
# from register 1 into bits of two and places them into reg 1 and reg 2
# from register 2 into bits of two and places them into reg 3 and reg 4
# from register 3 into bits of two and places them into reg 1 and reg 2
# from register 4 into bits of two and places them into reg 3 and reg 4

#Define the input file here
file_in = open("test.v", "r")

#define the output file here
file_out = open("output.v", "w")

#reading the input file
netlist = file_in.read()
file_in.close()

#converting the netlist to line by line format
netlist = netlist.split("\n")

def double_digit(half, full):
    for digit in half:
    	digit = str(digit)
    	digit = digit*2
    	#print digit
    	full += digit
    	#print full
    return full

def even_digits():
	pass

def reg_numbers(num, cnt_even, cnt_odd):
	if int(num) == 1:
		line[1] = line[1][:9] + "..." + line[1][9:] + "\n" + "8'd" + str(cnt_even) + ":CRPAT_Reg1<=10'b" + first_full + "\n" + "8'd" + str(cnt_even) + ":CRPAT_Reg2<=10'b" + second_full
	if int(num) == 2:
		line[1] = line[1][:9] + "..." + line[1][9:] + "\n" + "8'd" + str(cnt_even) + ":CRPAT_Reg3<=10'b" + first_full + "\n" + "8'd" + str(cnt_even) + ":CRPAT_Reg4<=10'b" + second_full
	if int(num) == 3:
		line[1] = line[1][:9] + "..." + line[1][9:] + "\n" + "8'd" + str(cnt_odd) + ":CRPAT_Reg1<=10'b" + first_full + "\n" + "8'd" + str(cnt_odd) + ":CRPAT_Reg2<=10'b" + second_full
	if int(num) == 4:
		line[1] = line[1][:9] + "..." + line[1][9:] + "\n" + "8'd" + str(cnt_odd) + ":CRPAT_Reg3<=10'b" + first_full + "\n" + "8'd" + str(cnt_odd) + ":CRPAT_Reg4<=10'b" + second_full
	#print line[1]

#iteration for line by line
cnt_even = 0
cnt_odd = 1
for line in netlist:

    line = line.split("=")
    if line[0] != "":    #prevents script from crashing when nothing in line
    	if len(line[0]) > 1:
	        if line[0][0] == "8" or line[0][1] == "8":
	            line[0] = "//" + line[0]
	            if line[1][0] != "2":
		            my_digits = line[1][:14]
		            #print my_digits
		            split_digits = my_digits.split("b")
		            first_half = split_digits[1][:5]
		            second_half = split_digits[1][5:]
		            first_full = ""
		            second_full = ""
		            first_full = double_digit(first_half, first_full)
		            second_full = double_digit(second_half, second_full)
		            findReg = line[0].split("_")
		            #print findReg
		            reg_num = findReg[1][3]
		            #print reg_num
		            reg_numbers(reg_num, cnt_even, cnt_odd)
		            cnt_even += 2
		            cnt_odd += 2
		            if cnt_even == 68 and cnt_odd == 69:
		            	cnt_even = 0
		            	cnt_odd = 1
		            #line[1] = reg_numbers(reg_num)
		            #line[1] = line[1][:9] + "..." + line[1][9:] + "\n" + "10'b" + first_full + "\n" + "10'b" + second_full
    line = "=".join(line)
    file_out.write(line+"\n")
    #file_out.write("10'b%s" % first_full)
    #file_out.write("10'b%s" % second_full)

file_out.close()
