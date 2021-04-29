import pandas as pd
import numpy as np

from Classes import Station

"""
S = ρ * 10000 - (20Nt + t / 10)
S: score
p: x amoutn of cities van de critical cities
Nt: total amount of trajectories (max 5)
t: time of all trajectories together
"""

def load_stations():
    stations = {}
    numbers = {}
    counter = 1

    with open("Stations.csv") as data:
        for row in data:
            row = row.strip("\n")
            row = row.strip(",")
            items = row.split(",")

            critical = False
            if len(items) == 4:
                critical = True

            stations[items[0]] = Station(items[0], float(items[1]), float(items[2]), critical)
            numbers[items[0]] = counter
            counter += 1

    return stations, numbers

def load_connections(stations):
    with open("Connection_Times.csv") as data:
        for row in data:
            row = row.strip("\n")
            items = row.split(",")

            stations[items[0]].add_connection(items[1], float(items[2]))
            stations[items[1]].add_connection(items[0], float(items[2]))

def distance_matrix(stations, numbers):
    i = len(stations.keys()) + 1
    matrix = np.zeros(shape=(i,i))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = np.inf

    for i in range(len(matrix[0])):
        matrix[0][i] = 0

    for station in stations:
        current_station = stations[station]
        current_num = numbers[station]

        for destination in current_station.connections:
            destination_num = numbers[destination]
            matrix[current_num][destination_num] = current_station.connections[destination]

    return matrix

def main():
    stations, numbers = load_stations()
    load_connections(stations)

    matrix = distance_matrix(stations, numbers)

    # print(stations["Zaandam"].connections)
    # print(matrix[numbers["Zaandam"]])




if __name__ == "__main__":
    main()