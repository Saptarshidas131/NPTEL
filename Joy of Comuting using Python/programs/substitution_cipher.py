"""
Description: Read a file and then cipher it and write it to another file.
Using substitution cipher(shift up or down by some number).
@author: Saptarshi Das
"""

import string

def substitute(filein,fileout,n):
    data = ""
    #opening a file for writing ciphered text
    fileout = open(fileout,"w")
    #dictionary of all the small and capital letters
    dict = {}
    for i in range(len(string.ascii_letters)):
        #substitute up by n(to go down n must be negative)
        dict[string.ascii_letters[i]] = string.ascii_letters[i-n]
    #print (dict)
    #opening input file for reading
    with open(filein) as f:
        while True:
            c = f.read(1)
            if not c:
                print ("----End of file----")
                break
            if c in dict:
                data  = dict[c]
            else:
                data = c
            fileout.write(data)
            #print the data of output file
            print (data)
    fileout.close()

try:
    fin =  input("Enter a valid input filename(include.txt): ")
    fout =  input("Enter a valid output filename(include.txt): ")
    n = int(input("Enter the number of shift(positive integer): "))
    if n<0:
        print ("Only negative shift possible, positive integer .")
    elif n==0:
        print ("0 shift, file unchanged.")
    else:
        substitute(fin,fout,n)

except:
    print ("Invalid Input or File.")

