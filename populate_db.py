from pymongo import MongoClient

def create_json(array):
    json=[]
    for element in array:
        networks=[]
        for network in element[1]:
            networks.append({
                "Address":network[0],
                "Signal":network[1],
                "Quality":network[2]
            })
        json.append({
            "coordinates":element[0],
            "networks":networks
        })
    return json 
def networks_json(pairs):
    networks=
    for pair in pairs:
        for wifi in par[1]:

def parse_file(name):
    pairs = []

    file = open(name,"r")
    file = file.readlines()

    count=0
    pairs_count = -1

    lat = ""
    lon = ""
    alt = ""
    sat = ""
    adr = ""
    sig = ""
    qlt = ""

    for line in file:
        line=line.rstrip(" ")
        if (line[len(line)-1]=="n"):
            line = line[:len(line)-2]
        if (count == 0):
            lat = line
            count=count+1
        elif (count == 1):
            lon = line
            count=count+1
        elif (count == 2):
            alt = line
            count=count+1
        elif (count == 3):
            sat = line
            pairs.append([[lat,lon,alt,sat],[]])
            pairs_count = pairs_count + 1
            count=count+1
        elif (count-4==0):
            if(not line[0]=="A"):
                count=1
                lat = line
            else:
                adr = line.split(" ")[1]
                count=count+1
        elif (count-4==1):
            sig = line.split(" ")[1]
            count=count+1
        elif (count-4==2):
            count=4
            qlt = line.split(" ")[1]
            pairs[pairs_count][1].append([adr,sig,qlt]) 
    return pairs
            

client = MongoClient('localhost', 27017)
db = client.wifipositioning
collection = db.data_pairs


pairs = parse_file("values.txt")
json = create_json(pairs)
collection.insert_many(json)
