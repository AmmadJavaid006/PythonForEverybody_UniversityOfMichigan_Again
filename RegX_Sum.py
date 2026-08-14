import re 

sum = 0

fname = input("Enter File Name: ")

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)
    quit()

for line in fhandle:
    if re.search("[0-9]+", line):
        y = re.findall("[0-9]+", line)
        for digit in y: 
            sum += int(digit)

#print(sum([int(x) for x in re.findall('[0-9]+', fhandle.read())]))

print(sum)