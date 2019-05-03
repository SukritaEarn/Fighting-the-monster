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
                                        model=self.world.war_wea)
        self.mon_wea_sprite = ModelSprite('images/mon_wea.png',
                                        model=self.world.mon_wea)
        self.war_icon_sprite = arcade.Sprite('images/war_icon.png', 1,
                                            center_x = 450, center_y = 530)
        self.mon_icon_sprite = arcade.Sprite('images/mon_icon.png', 1,
                                            center_x = 550, center_y = 530)
        self.sand_clock_sprite = arcade.Sprite('images/sand_clock.png', 0.3,
                                            center_x = 850, center_y = 300)
        self.power_sprite = Power(160, 310, 160, 310, 10)
        self.check_press = None
        self.reduce_mon_hp = Reduce_Mon_HP(925, 530, 0, 22)
        self.reduce_war_hp = Reduce_Mon_HP(75, 530, 0, 22)
        #self.miss1_sprite = Miss(120, 300)
        #self.miss2_sprite = Miss(850, 300)
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)
        self.power_sprite = Power(160, 310, 160, 310, 10)
        self.check_press = 1
        
    def on_mouse_release(self, x, y, button, modifiers):
        if not self.world.is_started():
            self.world.start()
        self.world.on_mouse_release(x, y, button, modifiers)
        self.check_press = 2

    def update(self, delta):
        self.world.update(delta)
        if self.check_press == 1:
            self.power_sprite.update(delta)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.war_wea_sprite.draw()
        self.mon_wea_sprite.draw()
        self.warrior_sprite.draw()
        self.monster_sprite.draw()

        arcade.draw_rectangle_filled(250, 530, 360, 32, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(450, 530, 33, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(250, 530, 350, 22, arcade.color.RED_BROWN)
        arcade.draw_circle_filled(450, 530, 28, arcade.color.RED_BROWN)
        self.war_icon_sprite.draw()
        
        arcade.draw_rectangle_filled(750, 530, 360, 32, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(550, 530, 33, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(750, 530, 350, 22, arcade.color.RED_BROWN)
        arcade.draw_circle_filled(550, 530, 28, arcade.color.RED_BROWN)
        self.mon_icon_sprite.draw()

        self.reduce_mon_hp.draw()
        self.reduce_war_hp.draw()
        
        if self.check_press == 1:
            self.power_sprite.draw()

        if self.check_press == 2:
            self.power_sprite.remove()

        # if self.world.war_wea.check_hit() in [1,2,3]:
        #     self.reduce_mon_hp.update()

        if

        if self.world.war_wea.check_hit() in [4,5]:
            #self.miss2_sprite.miss()
            pass

        # if self.world.mon_wea.check_hit() in [1,2,3]:
        #     self.reduce_war_hp.update()

        if self.world.mon_wea.check_hit() in [4,5]:
            #self.miss1_sprite.miss()
            pass

class Reduce_Mon_HP:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)

    def update(self):
        self.x -= 15
        self.width += 30

class Reduce_War_HP:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)

    def update(self):
        self.x += 15
        self.width += 30

class Miss:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def miss(self):
        arcade.Sprite('images/miss.png', 0.5, self.x , self.y)

    def update(self):
        pass

class Power:

    def __init__(self, x1, y1, x2, y2, width):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width

    def draw(self):
        arcade.draw_line(self.x1, self.y1, self.x2, self.y2, arcade.color.RED, self.width)

    def remove(self):
        self.width = 0

    def update(self, delta):
        self.x2 -= 1
        
def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
