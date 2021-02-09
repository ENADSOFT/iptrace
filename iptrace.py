import pygeoip
import socket

target = socket.gethostbyname("www.hackingloops.com")

print (target)


query = pygeoip.Geoip("GeoLiteCity.dat")

result = query.record_by_addr(target)

with open ("result.txt", "W") as file:
    file.write("[*] Query Results: \n\n")
    for


