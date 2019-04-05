import arcade.key
import math

class Warrior:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
    
    def update(self, delta):
        pass

class Monster:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass

class War_Wea:

    STARTING_VELOCITY = 10
    THROWING_VELOCITY = 10
    GRAVITY = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vy = War_Wea.STARTING_VELOCITY
        self.vx = War_Wea.STARTING_VELOCITY

    def throw(self, war, mon):
        start_x = war.x
        start_y = war.y
        dest_x = mon.x
        dest_y = mon.y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.vx = math.cos(angle) * War_Wea.THROWING_VELOCITY
        self.vy = math.sin(angle) * War_Wea.THROWING_VELOCITY

    def update(self, delta):
        self.x += self.vx
        self.y += self.vy
        if self.y == 550:
            self.y -= self.vy

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.warrior = Warrior(self, 120, 190)
        self.monster = Monster(self, 870, 270)
        self.war_wea = War_Wea(self, 120, 200)

    def on_key_press(self, key, key_modifiers):
        self.war_wea.throw(self.war_wea, self.monster)

    def update(self, delta):
        self.war_wea.update(delta)
