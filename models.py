import arcade.key

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
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.warrior = Warrior(self, 120, 190)
        self.monster = Monster(self, 870, 270)
        self.war_wea = War_Wea(self, 120, 200)
        
    def update(self, delta):
        self.warrior.update(delta)
