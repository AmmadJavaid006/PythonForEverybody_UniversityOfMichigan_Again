import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
repeat_value = int(input("Enter count: "))
position_value = int(input("Enter Position: "))

file = urllib.request.urlopen(url).read()

def link_follower(pos):
    be_file = BeautifulSoup(file, "html.parser")

    tags = be_file("a")
    lst = [tag.get("href", None) for tag in tags]
    print("Retrieving:", lst[pos - 1])
    return lst[pos - 1]

for i in range(repeat_value):
    url = link_follower(position_value)
    file = urllib.request.urlopen(url).read()

print("Last Name is:", url.split("known_by_")[1].replace(".html", ""))
