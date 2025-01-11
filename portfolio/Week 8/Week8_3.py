import sys

def grep(pattern, file_name):
    with open(file_name, 'r') as file:
        for line in file:
            if pattern in line:
                print(line, end='')  

def check():
    if len(sys.argv) != 3:
        print("Please provide both the pattern and the file name to search.")
    else:
        pattern = sys.argv[1]
        file_name = sys.argv[2]
        grep(pattern, file_name)

check()
