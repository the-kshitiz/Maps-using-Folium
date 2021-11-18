##Importing library
import folium
import pandas as pd

##Decalring dataframe and variables
location = pd.read_csv("Volcanoes_USA.txt")
lat = list(location.LAT)
lon = list(location.LON)
name = list(location.NAME)
elv = list(location.ELEV)

##Creating Map Object
map = folium.Map(location = [38.58, -99.09])

##function to decide the color of the marker depending on the elevation
def xyz(elev):
    if(elev<1000):
        return "green"
    elif(elev<2000):
        return "blue"
    else:
        return "red"

##Create FeatureGroup to add elements in Feature group instead of map to maintain modularity.
fg = folium.FeatureGroup(name="My Map")
for lt,ln,nm,el in zip(lat,lon,name,elv):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=nm, fill_color = xyz(el), color = "grey", radius= 10, fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005']> 100000000 else 'yellow'}))
map.add_child(fg)    

#Saving the map as Volcano.html
map.save("Volcano_Circle.html")