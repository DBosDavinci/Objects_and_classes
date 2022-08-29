class Pacperson:
    def __init__(self, score, direction, moving_speed):
        self.score = score
        self.direction = direction
        self.moving_speed = moving_speed
        self.lives = 3

    def move(self, direction):
        self.direction = direction

    def AddScore(self, score):
        self.score += score

    def RemoveLife(self, amount):
        self.lives -= amount

class Ghost:
    def __init__(self, killable, inactive, direction, moving_speed, color):
        self.killable = killable
        self.inactive = inactive
        self.direction = direction
        self.moving_speed = moving_speed
        self.color = color
    
    def Killed(self):
        self.inactive = True

    def Killable(self, killable):
        self.killable = killable

    def move(self, direction):
        self.direction = direction

    def Respawn(self):
        self.inactive = False

PacMan = Pacperson(0, None, 5)

Pinky = Ghost(False, True, None, 4, "pink")

Blinky = Ghost(False, True, None, 5, "red")