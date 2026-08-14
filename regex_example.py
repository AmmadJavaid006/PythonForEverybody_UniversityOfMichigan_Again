import re

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

atpos = x.find("@")
sppos = x.find(" ", atpos)

add = x[atpos+1 : sppos]

print(add)

y = re.findall("@([^ ]*)", x)
y = re.findall("200[0-9]+", x)
y = re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}", x) # Will even match HHH:MMM:SSS becuase of "greedy +" better to use "([0-9]{2}:[0-9]{2}:[0-9]{2})", "{2}" means will match two occurrence of the same regX

print(y)