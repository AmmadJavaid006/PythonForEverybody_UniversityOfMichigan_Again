import urllib, urllib.request, urllib.error, urllib.parse, xml.etree.ElementTree as xml

data = dict()

max1_count = None
max1_name = None

max2_count = None
max2_name = None

url = "http://py4e-data.dr-chuck.net/comments_42.xml"

file_read = urllib.request.urlopen(url).read().decode()

xml_file = xml.fromstring(file_read)

tag = xml_file.findall("comments/comment")

for name in tag:
    data.update({name.find("name").text : int(name.find("count").text)})
    for name, count in data.items():
        if max1_count is None or max1_count < count:
            max1_count = count
            max1_name = name

for name in tag:
    if max2_count is None or max2_count < int(name.find("count").text):
        max2_count = int(name.find("count").text)
        max2_name = name.find("name").text



print("The Person With the Highest Count is", max1_name, "with a count of", max1_count, "--> Dictionary version")

print("The Person With the Highest Count is", max2_name, "with a count of", max2_count, "--> Direct version")