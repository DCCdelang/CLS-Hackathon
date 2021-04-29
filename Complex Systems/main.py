from numpy.core.einsumfunc import _parse_einsum_input
import pandas as pd

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

    with open("Stations.csv") as data:
        for row in data:
            row = row.strip("\n")
            row = row.strip(",")
            items = row.split(",")

            critical = False
            if len(items) == 4:
                critical = True

            stations[items[0]] = Station(items[0], float(items[1]), float(items[2]), critical)
    
    return stations

def load_connections(stations):
    with open("Connection_Times.csv") as data:
        for row in data:
            row = row.strip("\n")
            items = row.split(",")

            stations[items[0]].add_connection(items[1], float(items[2]))
            stations[items[1]].add_connection(items[0], float(items[2]))


def main():
    stations = load_stations()
    load_connections(stations)


if __name__ == "__main__":
    main()