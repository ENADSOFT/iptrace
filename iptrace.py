import pygeoip
import socket

target = socket.gethostbyname("www.hackingloops.com")

print target


query = pygeoip.Geoip("GeoLiteCity.dat")


