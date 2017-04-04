import math

NORTH = 0
EAST  = 0.5 * math.pi
SOUTH = math.pi
WEST  = 1.5 * math.pi

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        pass

    def update_bearing(self, delta):
        self.bearing += delta 
        if self.bearing >= 2 * math.pi:
            self.bearing = self.bearing - 2 * math.pi
        elif self.bearing < 0:
            self.bearing = self.bearing + 2 * math.pi

    def turn_right(self):
        self.update_bearing(0.5 * math.pi)

    def turn_left(self):
        self.update_bearing(-0.5 * math.pi)

    def advance(self):
        self.x += int(math.sin(self.bearing))
        self.y += int(math.cos(self.bearing))
        self.coordinates = (self.x, self.y)

    def simulate(self, route):
        for act in route:
            if act == 'A':
                self.advance()
            elif act == 'R':
                self.turn_right()
            elif act == 'L':
                self.turn_left()