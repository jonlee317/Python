#This script takes variable sp and writes into excel with different corner information


import csv
import re

save_file = []

#Define the column titles
titles = ['pvt', 'vddl(V)', 'rscale', 'temp(C)', 'sp(V)']
save_file.append(titles)

#define the column values here
corners = {
    'rscale': ['typ', 'max', 'max', 'min', 'max', 'min', 'min', 'typ', 'typ', 'typ', 'typ'],
    'pvt': ['tt0', 'tt1', 'ss2', 'ss3', 'ss4', 'ff5', 'ff6', 'bnlp7', 'wnhp8', 'bpln9', 'wphn10'],
    'temp': ['85', '-40', '125', '125', '-40', '-40', '125', '125', '125', '125', '125'],
    'vddl': ['1.8', '1.52', '1.52', '1.52', '1.52', '1.98', '1.98', '1.52', '1.52', '1.52', '1.52'],
    'sp': [],   #Define your variable here
    }

#Define the input file here
file_in = open("input.out", "r")
        
#reading the input file
netlist = file_in.read()
file_in.close()

netlist = netlist.split("\n")
new_line = []
count = 0

for line in netlist:
    item = re.split(' ', line)
    if item[0] == 'sp=':    #searching for sp
        corners['sp'].append(item[1])   #taking numerical value of sp
        new_line.append(corners['pvt'][count])
        new_line.append(corners['vddl'][count])
        new_line.append(corners['rscale'][count])
        new_line.append(corners['temp'][count])
        new_line.append(corners['sp'][count])    #this is the sp
        print(new_line)
        save_file.append(new_line)
        new_line = []
        count += 1


#Output file name below
with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    #print writer
    writer.writerows(save_file)
