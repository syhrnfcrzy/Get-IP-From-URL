# Mencari sebuah IP dan Lokasi dari sebuah URL

import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("Masukan Sebuah URL: ")
IP = socket.gethostbyname(url)
response = DbIpCity.get(IP, api_key='free')
print("IP:", IP)
print("Kota:", response.city)
print("Negara:", response.region)
