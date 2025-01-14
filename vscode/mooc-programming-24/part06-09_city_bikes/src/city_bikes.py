# Write your solution here
import math

def get_station_data(filename: str):
    station={}
    with open (filename) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == "Longitude":
                continue
            latlong = (float(parts[0]), float(parts[1]))
            station[parts[3]]=latlong
    return station

def distance(stations: dict, station1: str, station2: str):
    for name, coord in stations.items():
        if name==station1:
            firstlon=coord[0]
            firstlat=coord[1]
        elif name==station2:
            seclon=coord[0]
            seclat=coord[1]

    x_km = (float(firstlon) - float(seclon)) * 55.26
    y_km = (float(firstlat) - float(seclat)) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    maxd = 0
    n1 = n2 = None
    
    # Obtendo todas as estações (pares de nome e coordenadas)
    for name1, coord1 in stations.items():
        for name2, coord2 in stations.items():
            if name1 != name2:  # Não calcular a distância de uma estação consigo mesma
                lon1, lat1 = coord1
                lon2, lat2 = coord2
                x_km = (float(lon1) - float(lon2)) * 55.26
                y_km = (float(lat1) - float(lat2)) * 111.2
                distance_km = math.sqrt(x_km**2 + y_km**2)

                if distance_km > maxd:
                    maxd = distance_km
                    n1, n2 = name1, name2  # Armazenar os nomes das estações com a maior distância

    return (n1, n2, maxd)


