import sys

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            print(f"The contents of {file1} and {file2} are the same.")
        else:
            print(f"The contents of {file1} and {file2} are different.")

def check():
    if len(sys.argv) != 3:
        print("Please provide both files name to compare and get the result.")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        compare_files(file1, file2)

check()
