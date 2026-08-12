    fname = input("Enter File Name: ")
    count = 0

    try:
        fhandle = open(fname, "r")
    except:
        print("File Not Found:", fname)
        quit()

    for line in fhandle:
        if line.startswith("From "): # the space in "From " handles the exception of From: as "From " matches with "From " but not with "From:"
            add = line.rstrip().split()
            count += 1
            print((add[1]))

    print("There were", count, "lines in the file with From as the first word")