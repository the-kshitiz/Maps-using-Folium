import folium
import pandas as pd
location = pd.read_csv("Volcanoes_USA.txt")
lat = list(location.LAT)
lon = list(location.LON)
name = list(location.NAME)
map = folium.Map(location = [38.58, -99.09])
fg = folium.FeatureGroup(name="My Map")
for lt,ln,nm in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon = folium.Icon(color = "green")))

map.add_child(fg)    
map.save("India.html")