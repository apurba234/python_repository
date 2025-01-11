import sys

def count_arguments():
    no_of_arguments = len(sys.argv[1:])
    print(f"Total number of arguments: {no_of_arguments}")

count_arguments()
