fname = input("Enter File Name: ")

mailers_info = dict()
freq_user = None
freq_user_count = None

try:
    fhandle = open(fname, "r")
except:
    print("File Not Found:", fname)
    quit()

for line in fhandle:
    if line.startswith("From "):
        parts = line.split()
        mail = parts[1]
        mailers_info[mail] = mailers_info.get(mail, 0) + 1

for mailer, count in mailers_info.items():
    if freq_user_count is None or count > freq_user_count:
        freq_user = mailer
        freq_user_count = count
    
print(freq_user, freq_user_count)