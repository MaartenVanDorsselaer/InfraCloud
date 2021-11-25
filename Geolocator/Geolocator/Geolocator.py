# !pip install geopy
# !pip install datetime
from geopy.geocoders import Nominatim
import folium
#
geolocator = Nominatim(user_agent="http://biasc.be")
#### Enter city and country
city_country = "Itterbeek, Belgium"
####
location = geolocator.geocode(city_country)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))
#
import datetime
print("Current date and time: ")
print(datetime.datetime.now())

coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap',  zoom_start=12)
map
# save method of Map object will create a map
# saved in Downloads
# map.save("geopy_location.html")
