import arcade
from models import World, Warrior

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('Model', None)
        super.__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.warrior_sprite = ModelSprite('images/warrior.png', model=self.world.warrior)
    
    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        
        self.warrior_sprite.draw()

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()