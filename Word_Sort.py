fname = input("Enter File Name: ")
fhandle = open(fname, "r")
words = list()

for line in fhandle:
    for word in line.rstrip().split(): 
        if word in words: continue
        words.append(word)

words.sort()
print(words)