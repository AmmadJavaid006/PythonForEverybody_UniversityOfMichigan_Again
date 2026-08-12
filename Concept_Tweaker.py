fname = input("Enter File Name: ")

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)
    quit()


words = dict()
bigword = None
bigcount = None


for data in fhandle:
    
    for word in data.split():
        words[word] = words.get(word, 0) + 1

for key,value in words.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value

print(bigword, bigcount)