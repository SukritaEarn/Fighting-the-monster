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
                                            center_x = 430, center_y = 530)
        self.mon_icon_sprite = arcade.Sprite('images/mon_icon.png', 1,
                                            center_x = 570, center_y = 530)
        self.miss_sprite1 = arcade.Sprite('images/miss.png', 0.3, 
                                        center_x = 880 , center_y = 350)
        self.miss_sprite2 = arcade.Sprite('images/miss.png', 0.3, 
                                        center_x = 110 , center_y = 350)
        self.boom_sprite1 = arcade.Sprite('images/boom.png', 0.5,
                                        center_x = 850, center_y = 230)
        self.boom_sprite2 = arcade.Sprite('images/boom.png', 0.5,
                                        center_x = 125, center_y = 210)
        self.sand_clock_sprite = arcade.Sprite('images/sand_clock.png', 0.3,
                                        center_x = 850, center_y = 350)
        self.vs_sprite = arcade.Sprite('images/vs.png', 0.18,
                                       center_x = 500 , center_y = 530)
        self.power_sprite = Power(160, 310, 160, 310, 10)
        self.check_press = None
        self.reduce_mon_hp = Reduce_Mon_HP(950, 530, 0, 22)
        self.reduce_war_hp = Reduce_War_HP(50, 530, 0, 22)
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)
        self.power_sprite = Power(160, 310, 160, 310, 10)
        self.check_press = 1
        
    def on_mouse_release(self, x, y, button, modifiers):
        if not self.world.is_started():
            self.world.start()
        self.world.on_mouse_release(x, y, button, modifiers)
        self.check_press = 2

    def wind_sprite(self, wind):
        if wind == 0:
            return
        elif wind == 1:
            return arcade.draw_triangle_filled(510, 455, 510, 465, 520, 460, arcade.color.ORANGE)
        elif wind == 2:
            return arcade.draw_triangle_filled(510, 455, 510, 465, 520, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(520, 455, 520, 465, 530, 460, arcade.color.ORANGE)
        elif wind == 3:
            return arcade.draw_triangle_filled(510, 455, 510, 465, 520, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(520, 455, 520, 465, 530, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(530, 455, 530, 465, 540, 460, arcade.color.ORANGE)
        elif wind == -1:
            return arcade.draw_triangle_filled(490, 455, 490, 465, 480, 460, arcade.color.ORANGE)
        elif wind == -2:
            return arcade.draw_triangle_filled(490, 455, 490, 465, 480, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(480, 455, 480, 465, 470, 460, arcade.color.ORANGE)
        elif wind == -3:
            return arcade.draw_triangle_filled(490, 455, 490, 465, 480, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(480, 455, 480, 465, 470, 460, arcade.color.ORANGE), arcade.draw_triangle_filled(470, 455, 470, 465, 460, 460, arcade.color.ORANGE)
        else:
            return

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
        self.vs_sprite.draw()

        arcade.draw_rectangle_filled(230, 530, 370, 32, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(230, 530, 360, 22, arcade.color.RED_BROWN)
   
        arcade.draw_rectangle_filled(770, 530, 370, 32, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(770, 530, 360, 22, arcade.color.RED_BROWN)

        self.reduce_mon_hp.draw()
        self.reduce_war_hp.draw()
        
        if self.check_press == 1:
            self.power_sprite.draw()
            if self.power_sprite.x2 <= 60:
                self.power_sprite.remove()

        if self.check_press == 2:
            self.power_sprite.remove()

        if self.world.war_wea.check_hit() == 1:
            self.reduce_mon_hp.update()
            self.boom_sprite1.draw()
            self.world.war_wea.kill()

        if self.world.war_wea.check_hit() == 0:
            self.miss_sprite1.draw()

        if self.world.mon_wea.check_hit() == 1:
            self.reduce_war_hp.update()
            self.boom_sprite2.draw()
            self.world.mon_wea.kill()

        if self.world.mon_wea.check_hit() == 0:
            self.miss_sprite2.draw()

        arcade.draw_circle_filled(430, 530, 33, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(430, 530, 28, arcade.color.RED_BROWN)
        self.war_icon_sprite.draw()

        arcade.draw_circle_filled(570, 530, 33, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(570, 530, 28, arcade.color.RED_BROWN)
        self.mon_icon_sprite.draw()

        arcade.draw_text('WIND', 479, 475, arcade.color.YELLOW, 14, bold=True)
        arcade.draw_circle_filled(500, 460, 5, arcade.color.YELLOW)
        self.wind_sprite(self.world.wind.wind)

        if self.reduce_mon_hp.width >= 360 or self.reduce_war_hp.width >= 360:
            self.world.dead()

        if self.world.is_dead():
            print('game over')

class Reduce_Mon_HP:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)

    def update(self):
        self.x -= 20
        self.width += 40

class Reduce_War_HP:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)

    def update(self):
        self.x += 20
        self.width += 40

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
