import json
import requests
import math


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def sort_by_distance(location):
    return location[0]


# Fetch the data from the URL
url = ('https://api2.hackclub.com/v0.1/Operations/Clubs?select={"fields":["Address Country","Name",'
       '"Latitude","Longitude","Slack Channel ID"]}')

getreq = requests.get(url)
obj = json.loads(getreq.content)

gps = []
names = []

# Extract latitude, longitude, and names from the fetched data
for x in obj:
    latitude = x['fields'].get('Latitude', [None])[0]
    longitude = x['fields'].get('Longitude', [None])[0]
    name = x['fields'].get('Name', None)
    if latitude is not None and longitude is not None:
        gps.append((float(latitude), float(longitude)))
        names.append(name)

# Pretty print the JSON data
str_out = json.dumps(obj, indent=4)
print(str_out)

# Print the GPS coordinates and names
print("GPS Coordinates:", gps)
print("Location Names:", names)

# Get user input for latitude, longitude, and maximum distance
lat = float(input("Enter Latitude: "))
long = float(input("Enter Longitude: "))
max_distance = float(input("Enter Maximum Distance (km): "))
user = (lat, long)

# Calculate distances
dist_list = [(haversine(user[0], user[1], pair[0], pair[1]), name, pair) for name, pair in zip(names, gps) if None not in pair]

# Filter locations within the maximum distance
filtered_locations = [item for item in dist_list if item[0] <= max_distance]

# Sort the filtered locations by distance
filtered_locations.sort(key=sort_by_distance)

# Get the three nearest locations
nearest_locations = filtered_locations[:3]

# Print the details of the three nearest locations
if nearest_locations:
    for i, (distance, name, coords) in enumerate(nearest_locations):
        google_maps_link = f"https://www.google.com/maps?q={coords[0]},{coords[1]}"
        print(f"Location {i+1}:")
        print("Name:", name)
        print("Distance:", round(distance,1), "km")
        print("Google Maps Link:", google_maps_link)
        print()
else:
    print("No locations found within the specified maximum distance.")