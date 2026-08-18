import urllib, urllib.request, urllib.error, urllib.parse, xml.etree.ElementTree as ET

sum = 0
count = 0

url = input("Enter Location: ")
file_read = urllib.request.urlopen(url).read().decode()

content = ET.fromstring(file_read)

lst = content.findall("comments/comment")

for i in lst:
    sum += int(i.find("count").text)
    count += 1

print("Retrieving", url)
print("Retrieved", len(file_read), "characters")
print("Count:", count)
print("Sum:", sum)