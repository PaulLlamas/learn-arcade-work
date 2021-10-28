import arcade
import random
import math

# --- Constants ---
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
MOVEMENT_SPEED = 10
PLAYER_SCALE = 0.8
SLIME_SCALE = 0.4
SLIME_COUNT = 30
FISH_SCALE = 0.4
FISH_COUNT = 30
BULLET_SPEED = 5
LASER_SCALE = 5
TARGET_SCALE = 2


class Slime(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Fish(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")

        self.set_mouse_visible(False)

        # Sprite lists
        self.player_list = None
        self.slime_list = None
        self.fish_list = None
        self.bullet_list = None
        self.target_list = None

        # Player Info
        self.player_sprite = None
        self.score = 0

        self.target_sprite = None

        self.set_mouse_visible(False)

        self.gun_sound = arcade.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.slime_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        # Character image from fandom.com in Pokemon Spectrum Wikia
        self.player_sprite = arcade.Sprite("Komodon.png", PLAYER_SCALE)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.target_sprite = arcade.Sprite("target.png", TARGET_SCALE)
        self.target_sprite.center_x = 60
        self.target_sprite.center_y = 60
        self.target_list.append(self.target_sprite)

        # Create the slimes
        for i in range(SLIME_COUNT):

            slime = Slime(":resources:images/enemies/slimeBlue_move.png", SLIME_SCALE)

            slime.center_x = random.randrange(SCREEN_WIDTH)
            slime.center_y = random.randrange(120, SCREEN_HEIGHT)
            slime.change_x = random.randrange(-3, 4)
            slime.change_y = random.randrange(-3, 4)

            self.slime_list.append(slime)

        for i in range(FISH_COUNT):

            fish = Fish(":resources:images/enemies/fishPink.png", FISH_SCALE)

            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(120, SCREEN_HEIGHT)
            fish.change_x = random. randrange(-3, 4)
            fish.change_y = random. randrange(-3, 4)

            self.fish_list.append(fish)

    def on_draw(self):

        arcade.start_render()
        self.player_list.draw()
        self.slime_list.draw()
        self.fish_list.draw()
        self.bullet_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.target_sprite.center_x = x
        self.target_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = arcade.Sprite("laserBlue01.png", LASER_SCALE)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y + 30
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet_angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.bullet_list.append(bullet)

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.hurt_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.upgrade_sound)

    def update(self, delta_time):
        self.slime_list.update()
        self.fish_list.update()
        self.bullet_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.slime_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fish_list)

        for slime in good_hit_list:
            slime.remove_from_sprite_lists()
            self.score += 1

        for fish in bad_hit_list:
            fish.remove_from_sprite_lists()
            self.score -= 1

        for bullet in self.bullet_list:

            good_hit_list = arcade.check_for_collision_with_list(bullet, self.slime_list)
            bad_hit_list = arcade.check_for_collision_with_list(bullet, self.fish_list)

            if len(good_hit_list) > 0:
                bullet.remove_from_sprite_lists()
                self.score += 1

            if len(bad_hit_list) > 0:
                bullet.remove_from_sprite_lists()
                self.score -= 1

            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
