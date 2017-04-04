NORTH = 0
EAST  = 90
SOUTH = 180
WEST  = 270

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        pass

    def update_bearing(self, delta):
        self.bearing += delta 
        self.bearing = self.bearing if self.bearing < 360 else self.bearing - 360
        self.bearing = self.bearing if self.bearing >= 0 else self.bearing + 360

    def turn_right(self):
        self.update_bearing(90)

    def turn_left(self):
        self.update_bearing(-90)

    def advance(self):
        pass

    def simulate(self, route):
        pass