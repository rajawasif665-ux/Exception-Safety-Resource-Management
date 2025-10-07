try:
    file=open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error:The file does not exist")