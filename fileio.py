
import sys
import os

# Simple program to read lines from file and append characters 'CN0' at the beginning of each line
#save file at end with changes.

#p1 = 'C'
#p2 = 'Users'
#p3 = 'IBM_ADMIN'
#p4 = 'Desktop'
# fpath =os.path.join(p1,p2)
# print(fpath)
# print(os.path.exists(fpath))
# testfile = open(fpath,"r")

#open input file in read only mode
In_File = open('input.txt', "r")

#open output file in write mode
Out_File = open('output.txt',"w")

#Read records from file
line = In_File.readline()

#format records
for line in In_File :
    #print ("before :",line,len(line))
    line = line.strip()
    line = "CN0" + line + "\n"
    #print("After : ",line,len(line))
    Out_File.write(line)

#Close files.
In_File.close()
Out_File.close()
