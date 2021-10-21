""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 799
MOVEMENT_SPEED = 10


class Strange:

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

    def strange_circle_draw(self):
        arcade.draw_circle_outline(self.position_x - 35, self.position_y - 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 30, self.position_y - 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 25, self.position_y - 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 20, self.position_y - 20, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 15, self.position_y - 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 10, self.position_y - 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x - 5, self.position_y - 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 5, self.position_y + 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 10, self.position_y + 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 15, self.position_y + 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 20, self.position_y + 20, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 25, self.position_y + 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 30, self.position_y + 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x + 35, self.position_y + 5, self.radius, self.color, 5)

    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.explosion_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.explosion_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.explosion_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.explosion_sound)


class Part2:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

    def part2_draw(self):
        arcade.draw_circle_outline(self.position_x, self.position_y - 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 20, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y - 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 5, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 20, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 15, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 10, self.radius, self.color, 5)
        arcade.draw_circle_outline(self.position_x, self.position_y + 5, self.radius, self.color, 5)

    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.explosion_sound)


        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.explosion_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.explosion_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.explosion_sound)


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        # Create our thing
        self.circle = Strange(60, 50, 0, 0, 50, arcade.color.BLUSH)
        self.linear_circle = Part2(60, 50, 0, 0, 50, arcade.color.SILVER)
        self.hurt_sound = arcade.load_sound(":resources:sounds/hurt2.wav")
        self.upgrade_sound = arcade.load_sound(":resources:sounds/upgrade5.wav")

    def on_draw(self):
        arcade.start_render()

        # Background
        arcade.set_background_color(arcade.csscolor.BLACK)
        arcade.draw_rectangle_outline(130, 130, 50, 200, arcade.csscolor.SNOW, 10, 45)
        arcade.draw_rectangle_outline(670, 670, 50, 200, arcade.csscolor.SNOW, 10, 45)
        arcade.draw_rectangle_outline(670, 130, 50, 200, arcade.csscolor.SNOW, 10, 135)
        arcade.draw_rectangle_outline(130, 670, 50, 200, arcade.csscolor.SNOW, 10, 135)
        arcade.draw_rectangle_outline(65, 400, 50, 425, arcade.csscolor.SNOW, 10)
        arcade.draw_rectangle_outline(735, 400, 50, 425, arcade.csscolor.SNOW, 10)
        arcade.draw_rectangle_outline(400, 735, 50, 425, arcade.csscolor.SNOW, 10, 90)
        arcade.draw_rectangle_outline(400, 65, 50, 425, arcade.csscolor.SNOW, 10, 90)

        self.circle.strange_circle_draw()
        self.linear_circle.part2_draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.circle.position_x = x
        self.circle.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.hurt_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.upgrade_sound)

    def update(self, delta_time):
        self.circle.update()
        self.linear_circle.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.linear_circle.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.linear_circle.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.linear_circle.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.linear_circle.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.linear_circle.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.linear_circle.change_y = 0


def main():
    window = MyGame()
    arcade.run()

main()