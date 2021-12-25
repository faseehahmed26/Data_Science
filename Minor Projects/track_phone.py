import phonenumbers
from test import my_num
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

ch_nmber=phonenumbers.parse(my_num)
loc=geocoder.description_for_number(ch_nmber,"en")
print(loc)

service_number=phonenumbers.parse(my_num,"RO")
print(carrier.name_for_number(service_number,"en"))


key='3e8a01cbb1c34c39ab44987989e9e365'
geocoder=OpenCageGeocode(key)
query=str(loc)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=loc).add_to(myMap)
myMap.save("mylocation.html")

