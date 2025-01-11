import sys

def wc(file_name):
    with open(file_name, 'r') as file:
        read_lines = file.readlines()
        number_of_lines = len(read_lines)  
        number_of_characters = sum(len(line) for line in read_lines)  

    print(f"Total number of Lines in the file is {number_of_lines}")
    print(f"Total number of Characters in the file is {number_of_characters}")

def check():
    if len(sys.argv) != 2:
        print("Please provide the file name as an argument.")
    else:
        file_name = sys.argv[1]
        wc(file_name)

check()
