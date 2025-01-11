import sys

def backup_file():
    if len(sys.argv) != 2:
        print("Enter both the file name you want to create a backup of.")
        sys.exit(1)  

    filename = sys.argv[1]
    backup_filename = filename + "_backup.txt"

    with open(filename, 'r') as original_file:
        with open(backup_filename, 'w') as backup_file:
            backup_file.write(original_file.read())  

    print(f"Backup of {filename} is {backup_filename}.")


backup_file()
