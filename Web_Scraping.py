import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

sum = 0
count = 0
url = input("Enter URL: ")
fhandle = urllib.request.urlopen(url)
file = urllib.request.urlopen(url).read()

be_file = BeautifulSoup(file, "html.parser")
spans = be_file("span")

for span in spans:
    sum += int(span.contents[0])
    count += 1

print(sum)
print(count)