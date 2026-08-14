import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

#fhandle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
fhandle = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
file = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm").read()
soup = BeautifulSoup(file, "html.parser")

word_count = dict()

tags = soup("a")

for tag in tags:
    print(tag.get("href", None))
    

for line in fhandle:
    words = line.decode().split() # Use split() and not strip(), strip removes the white-spaces while split breaks every line down to single characters
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    if re.search(r'href="([^"]+)', line.decode()):
        print(re.findall(r'href="([^"]+)', line.decode()))

print(word_count)

