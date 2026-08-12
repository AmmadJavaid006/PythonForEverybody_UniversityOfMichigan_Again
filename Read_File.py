fname = input("Enter File Name: ")

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)
    quit()

for line in fhandle:
    print(line.upper().rstrip())