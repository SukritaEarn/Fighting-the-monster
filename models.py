import arcade
import math
import time
import random

class Warrior:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
    
    def update(self, delta):
        pass

class Monster:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, delta):
        pass

class War_HP:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        
    def update(self, delta):
        pass

class Mon_HP:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        
    def update(self, delta):
        pass

class War_Wea:

    VELOCITY_X = 10
    VELOCITY_Y = 0
    GRAVITY = 0.088

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = War_Wea.VELOCITY_X
        self.vy = War_Wea.VELOCITY_Y
        self.angle = 0

    def throw(self, war, mon):
        self.vy = (World.END_TIME - World.START_TIME)*5

    def check_hit(self, mon):
        if 160 <= self.y <= 340:
            return True
        return False

    def update(self, delta):
        self.x += self.vx
        self.y += self.vy
        self.vy -= War_Wea.GRAVITY
        self.angle -= 1

class Mon_Wea:

    VELOCITY_X = 10
    VELOCITY_Y = random.randint(2,7)
    GRAVITY = 0.088
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = Mon_Wea.VELOCITY_X
        self.vy = Mon_Wea.VELOCITY_Y
        self.angle = 0

    def update(self, delta):
        self.x -= self.vx
        self.y += self.vy
        self.vy -= Mon_Wea.GRAVITY
        self.angle += 0.7

class World:

    STATE_FROZEN = 1
    STATE_STARTED = 2
    START_TIME = 0
    END_TIME = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = World.STATE_FROZEN
        
        self.warrior = Warrior(self, 120, 210)
        self.monster = Monster(self, 850, 230)
        self.war_wea = War_Wea(self, 120, 250)
        self.mon_wea = Mon_Wea(self, 850, 250)
        self.war_hp = War_HP(self, 450, 530)
        self.mon_hp = Mon_HP(self, 550, 530)

    def start(self):
        self.state = World.STATE_STARTED
 
    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def reset(self):
        self.war_wea.x = 120
        self.war_wea.y = 250
        self.war_wea.vx = 10
        self.war_wea.vy = 0
        self.war_wea.angle = 0
        self.mon_wea.x = 850
        self.mon_wea.y = 250
        self.mon_wea.vx = 10
        self.mon_wea.vy = random.randint(2,7)
        self.mon_wea.angle = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            World.START_TIME = time.time()

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            World.END_TIME = time.time()
            self.war_wea.throw(self.warrior, self.monster)

    def update(self, delta):
        if self.state == World.STATE_STARTED:
            self.war_wea.update(delta)
        if self.war_wea.x >= self.monster.x:
            self.mon_wea.update(delta)
        if self.mon_wea.x <= -35:
            self.state = World.STATE_FROZEN
            self.reset()
