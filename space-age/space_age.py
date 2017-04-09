def earth_years(seconds):
     return seconds / 31557600

def convert(planet, seconds):
    converter = {        
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1,
        'Mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus':  84.016846,
        'neptune': 164.79132
        }
    return earth_years(seconds) * converter[planet]

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        pass

    def __getattr__(self, attr):
        if attr.startswith('on_'):
            def wrapper():
                return convert(attr[3:], self.seconds)

            return wrapper
