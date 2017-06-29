from pymongo import MongoClient
import gmplot

colors = ['b', 'g','r','c','m','y','k','w']
c_count = 0

def get_coords(data):
    #data = collection.find_one({"address":address})
    networks = data["networks"]
    lats = []
    lons = []
    for network in networks:
        coordinates = network["coordinates"]
        lat = coordinates["lat"].rstrip("\n ").strip(" ")
        lon = coordinates["lon"].rstrip("\n ").strip(" ")
        print lat,",",lon
        lats.append(float(lat))
        lons.append(float(lon))
    return [lats,lons]

client = MongoClient('localhost', 27017)
db = client.wifipositioning
collection = db.by_address

gmap = gmplot.GoogleMapPlotter(33.7855766667, -84.3751076667, 14)

for item in collection.find({}):
    latlon=get_coords(item)
    gmap.scatter(latlon[0], latlon[1], colors[c_count%len(colors)], marker=True)
    c_count+=1 

gmap.draw("mymap.html")