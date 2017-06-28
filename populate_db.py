from pymongo import MongoClient

def address_first_json(array):
    json = []
    by_address = {}
    for element in array:
        for network in element[1]:
            address=network[0]
            if address not in by_address.keys():
                by_address[address]=[[element[0],network]]
            else:
                by_address[address].append([element[0],network])
    print by_address.keys()
    json=[]
    for key in by_address.keys():
        address = key
        networks =[]
        for element in by_address[key]:
            network = element[1]
            network_json = {
            "Address":network[0],
            "Signal":network[1],
            "Quality":network[2]
            }
            coordinates_json = {
            "lat":element[0][0],"lon":element[0][1],"alt":element[0][2],"sat":element[0][3]
            }
            pair_json = {
                "coordinates":coordinates_json,
                "network":network_json
            }
            networks.append(pair_json)
        json.append({
        "address":address,
        "networks": networks
        })
    return json
    

    
                
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
        coordinates = {
            "lat":element[0][0],"lon":element[0][1],"alt":element[0][2],"sat":element[0][3]
        }
        json.append({
            "coordinates":coordinates,
            "networks":networks
        })
    return json 

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
#json = create_json(pairs)
#collection.insert_many(json)

json = address_first_json(pairs)
collection = db.by_address
collection.insert_many(json)
