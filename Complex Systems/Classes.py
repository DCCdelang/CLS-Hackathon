
class Station():
    def __init__(self, name, x, y, critical):
        self.name = name
        self.x = x
        self.y = y
        self.critical = critical
        self.connections = {}


    def add_connection(self, city, time):
        self.connections[city] = time