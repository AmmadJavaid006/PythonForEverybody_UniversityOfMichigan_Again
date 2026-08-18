import urllib, urllib.request, urllib.parse, urllib.error, json

url = input("Enter Location: ")

result = urllib.request.urlopen(url).read().decode()

jfile = json.loads(result)

sum = 0
count = 0

for item in jfile["comments"]:
    sum += item["count"]
    count += 1

print("Retrieving:", url)
print("Retrieved", len(result), "characters")
print("Count:", count)
print("Sum:", sum)