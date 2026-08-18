import urllib, urllib.parse, urllib.request, json

api = "http://py4e-data.dr-chuck.net/opengeo?"
location = input("Enter location: ")

dict = dict()
dict["q"] = location

formatted_url = api + urllib.parse.urlencode(dict)
response = urllib.request.urlopen(formatted_url).read().decode()
jfile = json.loads(response)

print("Retrieving:", formatted_url  )
print("Retrieved", len(response), "characters")
print("Plus Code", jfile["features"][0]["properties"]["plus_code"])
