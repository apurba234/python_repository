import sys

def nl(file_name):
    with open(file_name, 'r') as file:
        line_number = 1
        for line in file:
            print(f"{line_number}  {line}", end='')  
            line_number += 1

def check():
    if len(sys.argv) != 2:
        print("Invalid. Please enter both the python script name and the file name to check.")
    else:
        filename = sys.argv[1]
        nl(filename)
check()
