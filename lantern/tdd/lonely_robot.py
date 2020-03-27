class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction

        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        elif self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {
            "E": "N",
            "N": "W",
            "W": "S",
            "S": "E"
        }
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {
            "W": "N",
            "S": "W",
            "E": "S",
            "N": "E"
        }
        self.direction = turns[self.direction]

    def move_forward(self):
        if self.direction == "W":
            self.x -= 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1

        return self.y+self.x

    def move_back(self):
        if self.direction == "W":
            self.x += 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1

        if self.x > self.asteroid.x or self.y > self.asteroid.y or self.x < 1 or self.y < 1:
            raise RobotHasFallFromAsteroidError()
        else:
            return self.y+self.x

class MissAsteroidError(Exception):
    pass

class RobotHasFallFromAsteroidError(Exception):
    pass