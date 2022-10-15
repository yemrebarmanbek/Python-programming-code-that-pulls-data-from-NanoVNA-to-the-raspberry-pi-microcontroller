#first use "sed -i 's/\x0//g' filename.txt" from command to eliminate null characters 

from numpy import array
import numpy as np
import csv
import skrf as rf

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


with open('prove_array_calibrazione.txt', encoding="utf8", errors='ignore') as f:

    arr = ""
    for line in f:
        arr += line.replace("\n", ",") ## Replace each newline character in each line so that arr is just one long continuous string
    arr = eval(arr) ## The text will now be stored as a list
    arr = array( arr ) ## Now it's a numpy array (hopefully)
    
        
text_path = '/home/pi/progetto/nanovna_data/Thu May 26 23-17-10 2022.s2p'
ntwk = rf.Network(text_path)
s = ntwk.s

s11 = ntwk.s[:,0,0]  # get first 10 values of S21
Modulo = np.abs(s11)
value = np.dot(arr, Modulo)

append_new_line('values.txt', str(value))


    
    