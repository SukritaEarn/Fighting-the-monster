class Warrior:
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
        
        self.warrior = Warrior(self, 60, 100)
    
    def update(self, delta):
        self.warrior.update(delta)
