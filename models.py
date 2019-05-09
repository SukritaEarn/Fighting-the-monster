import arcade
import time
import random

class Warrior:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
    
    def update(self, delta):
        self.angle += 1

class Monster:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, delta):
        self.angle += 1

class War_Wea:

    VELOCITY_X = 10
    VELOCITY_Y = 0
    GRAVITY = 0.3
    THROW_WAIT = 2

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = War_Wea.VELOCITY_X
        self.vy = War_Wea.VELOCITY_Y
        self.angle = 0

    def throw(self, start, end):
        if end - start >= 7:
            start = 0
            end = 0
        self.vy = (end - start)*5
    
    def kill(self):
        self.x = 2000
        self.y = 2000

    def check_hit(self):
        if 120 <= self.y <= 340 and 820 <= self.x <= 850:
            return 1
        if self.y >= 341 and 850 <= self.x <= 1000:
            return 0
        if self.y <= 119 and 850 <= self.x <= 1000:
            return 0

    def update(self, delta):
        self.x += self.vx
        self.y += self.vy
        self.vy -= War_Wea.GRAVITY
        self.angle -= 1
        
class Mon_Wea:

    VELOCITY_X = 10
    VELOCITY_Y = random.randint(10,11)
    GRAVITY = 0.3
    THROW_WAIT = 1
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = Mon_Wea.VELOCITY_X
        self.vy = Mon_Wea.VELOCITY_Y
        self.angle = 0
        self.wait_time = 0

    def kill(self):
        self.x = -2000
        self.y = -2000

    def check_hit(self):
        if 110 <= self.y <= 300 and 120 <= self.x <= 150:
            return 1
        if self.y >= 301 and 0 <= self.x <= 150:
            return 0
        if self.y <= 109 and 0 <= self.x <= 150:
            return 0

    def update(self, delta):
        self.wait_time += delta
        if self.wait_time < Mon_Wea.THROW_WAIT:
            return
        self.x -= self.vx
        self.y += self.vy
        self.vy -= Mon_Wea.GRAVITY
        self.angle += 0.7

class Wind:
    
    def __init__(self, world, wind):
        self.world = world
        self.wind = wind

    def update(self):
        self.wind = random.randint(-3,3)

class World:

    STATE_FROZEN = 1
    STATE_STARTED = 2
    NO_TURN = 0
    WAR_TURN = 1
    MON_TURN = 2
    START_TIME = 0
    END_TIME = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = World.STATE_FROZEN
        self.turn = World.NO_TURN
        self.warrior = Warrior(self, 120, 210)
        self.monster = Monster(self, 850, 230)
        self.war_wea = War_Wea(self, 120, 250)
        self.mon_wea = Mon_Wea(self, 850, 250)
        self.wind = Wind(self, random.randint(-3,3))
        self.war_wea.vy += self.wind.wind
        self.mon_wea.vy -= self.wind.wind

    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def is_war_turn(self):
        return self.turn == World.WAR_TURN

    def reset(self):
        self.wind.update()
        self.war_wea.x = 120
        self.war_wea.y = 250
        self.war_wea.vx = 10
        self.war_wea.vy = 0 + self.wind.wind
        self.war_wea.angle = 0
        self.mon_wea.x = 850
        self.mon_wea.y = 250
        self.mon_wea.vx = 10
        self.mon_wea.vy = random.randint(10,11) - self.wind.wind
        self.mon_wea.angle = 0
        self.mon_wea.wait_time = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.turn == World.NO_TURN:
            self.turn = World.WAR_TURN
            if button == arcade.MOUSE_BUTTON_LEFT:
                World.START_TIME = time.time()
        else:
            World.START_TIME = 0

    def on_mouse_release(self, x, y, button, modifiers):
        if self.turn == World.WAR_TURN:
            if button == arcade.MOUSE_BUTTON_LEFT:
                World.END_TIME = time.time()
                self.war_wea.throw(World.START_TIME, World.END_TIME)
            self.turn = World.MON_TURN
        else:
            World.END_TIME = 0

    def update(self, delta):
        if self.state == World.STATE_STARTED:
            self.war_wea.update(delta)
        if self.war_wea.x >= self.monster.x - 50:
            self.mon_wea.update(delta)
        if self.mon_wea.x <= -35 or self.mon_wea.y == -1000:
            self.state = World.STATE_FROZEN
            self.turn = World.NO_TURN
            self.reset()
