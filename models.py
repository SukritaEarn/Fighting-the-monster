import arcade.key
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

class War_Wea:

    VELOCITY_X = 10
    VELOCITY_Y = 0

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = War_Wea.VELOCITY_X
        self.vy = War_Wea.VELOCITY_Y
        self.h = 0
        self.angle = 0

    def throw(self, war, mon):
        start_x = war.x
        start_y = war.y
        dest_x = mon.x
        dest_y = mon.y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.vy = (World.END_TIME - World.START_TIME)*8
        self.h = ((self.vy**2)*(math.sin(2*angle)))

    def update(self, delta):
        self.x += self.vx
        self.y += self.vy
        if self.y >= 580:
            self.vy = -self.vy
            self.angle -= 90

class Mon_Wea1:

    VELOCITY_X = 10
    VELOCITY_Y = random.randint(6,9)

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = Mon_Wea1.VELOCITY_X
        self.vy = Mon_Wea1.VELOCITY_Y
        self.h = 0
        self.angle = 0

    def throw(self, war, mon):
        start_x = war.x
        start_y = war.y
        dest_x = mon.x
        dest_y = mon.y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.vy = (World.END_TIME - World.START_TIME)*8
        self.h = ((self.vy**2)*(math.sin(2*angle)))

    def update(self, delta):
        self.x -= self.vx
        self.y += self.vy
        if self.y >= 580:
            self.vy = -self.vy
            self.angle = 90

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
        self.war_wea = War_Wea(self, 120, 200)
        self.mon_wea1 = Mon_Wea1(self, 850, 200)

    def start(self):
        self.state = World.STATE_STARTED
 
    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    #def on_mouse_motion(self, x, y, dx, dy):
        #self.war_wea.x = x
        #self.war_wea.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            World.START_TIME = time.time()

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            World.END_TIME = time.time()
            self.war_wea.throw(self.warrior, self.monster)
            print(World.END_TIME - World.START_TIME)
            print(self.war_wea.vy)
            print(self.war_wea.h)

    def update(self, delta):
        if self.state == World.STATE_STARTED:
            self.war_wea.update(delta)
        if self.war_wea.x >= self.width:
            self.mon_wea1.update(delta)
