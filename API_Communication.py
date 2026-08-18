import urllib, urllib.request, urllib.parse, urllib.error, json

first_part_url = "https://py4e-data.dr-chuck.net/opengeo?"

while True:

    location = input("Enter Location: ")

    location = location.strip()
    dict = dict()

    dict["q"] = location

    url = first_part_url + urllib.parse.urlencode(dict)
    result = urllib.request.urlopen(url).read().decode()

    jfile = json.loads(result)

    print("Longitude:", jfile["features"][0]["properties"]["lon"])
    print("Latitude:", jfile["features"][0]["properties"]["lat"])
    location = jfile["features"][0]["properties"]["formatted"]
    print("Location:", location)
    print("Country:", jfile["features"][0]["properties"]["country"])