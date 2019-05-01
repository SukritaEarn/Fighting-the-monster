import arcade
from models import World, Warrior, Monster

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Fighting the monster'

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture('images/bg.png')
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.warrior_sprite = ModelSprite('images/warrior.png', 
                                        model=self.world.warrior)
        self.monster_sprite = ModelSprite('images/mon.png',
                                        model=self.world.monster)
        self.war_wea_sprite = ModelSprite('images/war_wea.png',
                                        model=self.world.war_wea1)
        self.mon_wea1_sprite = ModelSprite('images/mon_wea1.png',
                                        model=self.world.mon_wea1)
    #def on_mouse_motion(self, x, y, dx, dy):
         #self.world.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if not self.world.is_started():
            self.world.start()
        self.world.on_mouse_release(x, y, button, modifiers)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.war_wea_sprite.draw()
        self.mon_wea1_sprite.draw()
        self.warrior_sprite.draw()
        self.monster_sprite.draw()

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
