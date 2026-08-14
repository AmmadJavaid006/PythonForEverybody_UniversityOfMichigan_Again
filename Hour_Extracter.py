fname = input("Enter the filename: ")

hours_count = dict()
lst = list()

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)

for line in fhandle:
    if line.startswith("From "):
        sep_data = line.split()
        hours = sep_data[5].split(":")
        hours_count[hours[0]] = hours_count.get(hours[0], 0) + 1

#lst = sorted([(k, v) for k, v in hours_count.items()]) Another Way to perform the below task "for loop and sort both"

for k, v in hours_count.items():
    lst.append((k, v))
lst.sort()

for v, k in lst: 
    print(v, k)