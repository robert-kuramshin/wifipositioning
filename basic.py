file = open("values.txt","r")
file = file.readlines()
count=0
pairs_count = -1
pairs = []
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
    elif (count == 1):
        lon = line
    elif (count == 2):
        alt = line
    elif (count == 3):
        sat = line
        pairs.append([[lat,lon,alt,sat],[]])
        pairs_count = pairs_count + 1
    elif (count-4==0):
        if(not line[0]=="A"):
            pairs[pairs_count][1].append[adr,sig,qlt] 
        adr = line
    elif (count-4==1):
        sig = line
    elif (count-4==2):
        count=4
        qlt = line
        pairs[pairs_count][1].append([adr,sig,qlt]) 
    count=count+1
print pairs
        
