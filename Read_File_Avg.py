spam_confidence = 0
total = 0

fname = input("Enter File Name: ")

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)
    quit()

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    colon_ind = line.find(":")
    spam_confidence_it = float(line[colon_ind + 1 : ])
    spam_confidence += spam_confidence_it
    total += 1

avg = spam_confidence / total

print("Average spam confidence:", avg)