import arcade
import math

SPRITE_SCALING = 0.15
SPRITE_NATIVE_SIZE = 528
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SWORD_SCALE = 0.05
SWORD_SPEED = 10

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Lab 12 Project"
SKE_ICON = 5
LIVES = 1
MOVEMENT_SPEED = 3.5
UPDATES_PER_FRAME = 2

GRAVITY = 2.5
P_JUMP = 25

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

CHARACTER_SCALING = 5

# Skyrim soundtrack "Dragonborn"
background_soundtrack = arcade.sound.load_sound("Dragonborn.wav")


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to The Dungeon", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("The Mighty Kingdom sent you to clean the dungeon", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("and collect the skeletons of previous mighty people",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Kill all monsters and collect the skeletons!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Use A and D to move, mouse to aim, and click to shoot", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 + 75, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Use W to jump.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class PlayerCharacter(arcade.Sprite):

    def __init__(self):
        # Set up parent class
        super().__init__(hit_box_algorithm='Simple')

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self._points = [[-22, -220], [22, -220], [22, 192], [-22, 192]]

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair("soldier_idle.png")

        self.walk_textures = []
        for i in range(16):
            texture = load_texture_pair(f"soldier_run-{i}.png")
            self.walk_textures.append(texture)

        self.scale = SPRITE_SCALING

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 15 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]


class Room:

    def __init__(self):

        self.wall_list = None

        self.background = None


class Coin(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.coin_list = None


class Enemy(arcade.Sprite):

    def __init__(self):
        # Set up parent class
        super().__init__(hit_box_algorithm='Simple')

        self.scale = SPRITE_SCALING

        self.change_x = 0

        self.enemy_list = None

    def update(self):

        self.center_x += self.change_x

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1


def setup_room_1():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("wall1.png",
                                 SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("wall1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
    brick.left = SPRITE_SIZE
    brick.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(brick)

    for x in range(180, 830, 120):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 300
        room.wall_list.append(brick)
    for x in range(180, 830, 120):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 550
        room.wall_list.append(brick)

    coordinate_list = [[1000, 285], [1000, 225], [1000, 165], [1000, 110], [945, 225], [945, 165], [945, 110],
                       [890, 165], [890, 110], [835, 110]]

    for coordinate in coordinate_list:
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.55)
        brick.center_x = coordinate[0]
        brick.center_y = coordinate[1]
        room.wall_list.append(brick)

    room.background = arcade.load_texture("dun1.png")

    return room


def setup_coins_1():
    coin = Coin()
    coin.coin_list = arcade.SpriteList()
    for x in range(180, 830, 120):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = 600
        coin.coin_list.append(coins)
    for x in range(300, 800, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


def enemy_setup_1():
    enemy = Enemy()
    enemy.enemy_list = arcade.SpriteList()
    enemies = arcade.Sprite("metalslug_zombie-1.png", SPRITE_SCALING * 2.2)
    enemies.center_x = (SCREEN_WIDTH - (SPRITE_SIZE - 25))
    enemies.bottom = SPRITE_SIZE * 4
    enemy.enemy_list.append(enemies)

    return enemy


def golden_setup1():
    golden = Coin()
    golden.golden_list = arcade.SpriteList()
    golden_skeleton = arcade.Sprite("goldenskeleton.png", SPRITE_SCALING * 1.4)
    golden_skeleton.center_x = (SCREEN_WIDTH - (SPRITE_SIZE - 25))
    golden_skeleton.bottom = SPRITE_SIZE * 4
    golden.golden_list.append(golden_skeleton)

    return golden


def setup_room_2():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("wall1.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0 and x == 0:
                wall = arcade.Sprite("wall1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # --- Place walls with a list
    coordinate_list = [[110, 285], [110, 225], [110, 165], [110, 110], [165, 225], [165, 165], [165, 110],
                       [220, 165], [220, 110], [220, 110], [275, 110]]

    # Loop through coordinates
    for coordinate in coordinate_list:
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.55)
        brick.center_x = coordinate[0]
        brick.center_y = coordinate[1]
        room.wall_list.append(brick)

    # --- Place boxes inside a loop
    for x in range(300, 950, 150):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 350
        room.wall_list.append(brick)

    room.background = arcade.load_texture("dun2.jpg")

    return room


def setup_coins_2():
    coin = Coin()
    coin.coin_list = arcade.SpriteList()
    for x in range(300, 950, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = 400
        coin.coin_list.append(coins)
    for x in range(400, 1050, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


def enemy_setup_2():
    enemy = Enemy()
    enemy.enemy_list = arcade.SpriteList()
    for x in range((SPRITE_SIZE * 5), (SCREEN_WIDTH - SPRITE_SIZE), 120):
        enemies = arcade.Sprite("metalslug_zombie-1.png", SPRITE_SCALING * 2.2)
        enemies.center_x = x
        enemies.bottom = SPRITE_SIZE
        enemy.enemy_list.append(enemies)

    return enemy


def golden_setup2():
    golden = Coin()
    golden.golden_list = arcade.SpriteList()
    golden_skeleton = arcade.Sprite("goldenskeleton.png", SPRITE_SCALING * 1.4)
    golden_skeleton.center_x = (SCREEN_WIDTH - (SPRITE_SIZE - 25))
    golden_skeleton.bottom = SPRITE_SIZE * 4
    golden.golden_list.append(golden_skeleton)

    return golden


def setup_room_3():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("wall1.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("wall1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    coordinate_list = [[110, 285], [110, 225], [110, 165], [110, 110], [165, 225], [165, 165], [165, 110], [220, 165],
                       [220, 110], [220, 110], [275, 110]]

    for coordinate in coordinate_list:
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.55)
        brick.center_x = coordinate[0]
        brick.center_y = coordinate[1]
        room.wall_list.append(brick)

    for x in range(300, 950, 150):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 350
        room.wall_list.append(brick)

    room.background = arcade.load_texture("dun3.jpg")

    return room


def setup_coins_3():
    coin = Coin()
    coin.coin_list = arcade.SpriteList()
    for x in range(300, 950, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = 400
        coin.coin_list.append(coins)
    for x in range(400, 1050, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


def enemy_setup_3():
    enemy = Enemy()
    enemy.enemy_list = arcade.SpriteList()
    for x in range((SPRITE_SIZE * 5), (SCREEN_WIDTH - SPRITE_SIZE), 240):
        enemies = arcade.Sprite("metalslug_zombie-1.png", SPRITE_SCALING * 2.2)
        enemies.center_x = x
        enemies.bottom = SPRITE_SIZE
        enemy.enemy_list.append(enemies)

    return enemy


def golden_setup3():
    golden = Coin()
    golden.golden_list = arcade.SpriteList()
    golden_skeleton = arcade.Sprite("goldenskeleton.png", SPRITE_SCALING * 1.4)
    golden_skeleton.center_x = (SCREEN_WIDTH - (SPRITE_SIZE * 3))
    golden_skeleton.bottom = SPRITE_SIZE * 5
    golden.golden_list.append(golden_skeleton)

    return golden


class GameView(arcade.View):

    def __init__(self):

        super().__init__()

        # Sprite lists
        self.current_room = 0
        self.room_coins = 0
        self.enemy_room = 0
        self.golden_room = 0

        # Set up the player
        self.player_sprite = None
        self.player_list = None
        self.sword_list = None

        # Set up the scene
        self.rooms = None
        self.coins = None
        self.enemies = None
        self.golden = None

        # Set up logic
        self.physics_engine = None
        self.dead_hit_list = None

        # Set up controls
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set up counts
        self.lives = LIVES
        self.score = 0
        self.time_taken = 0

        # Set up sounds
        self.good_hit_sound = arcade.sound.load_sound(":resources:sounds/coin1.wav")

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.sword_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = SPRITE_SIZE * 2
        self.player_sprite.center_y = SPRITE_SIZE * 1.5
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []
        self.coins = []
        self.enemies = []
        self.golden = []

        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        coins = setup_coins_1()
        self.coins.append(coins)

        coins = setup_coins_2()
        self.coins.append(coins)

        coins = setup_coins_3()
        self.coins.append(coins)

        enemies = enemy_setup_1()
        self.enemies.append(enemies)

        enemies = enemy_setup_2()
        self.enemies.append(enemies)

        enemies = enemy_setup_3()
        self.enemies.append(enemies)

        golden = golden_setup1()
        self.golden.append(golden)

        golden = golden_setup2()
        self.golden.append(golden)

        golden = golden_setup3()
        self.golden.append(golden)

        # Our starting room number
        self.current_room = 0
        self.room_coins = 0
        self.enemy_room = 0
        self.golden_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list,
                                                             gravity_constant=GRAVITY)

    def on_draw(self):

        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        self.rooms[self.current_room].wall_list.draw()

        self.coins[self.room_coins].coin_list.draw()

        self.enemies[self.enemy_room].enemy_list.draw()

        self.player_list.draw()

        self.sword_list.draw()

        if len(self.enemies[self.enemy_room].enemy_list) == 0:
            self.golden[self.golden_room].golden_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 30)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = P_JUMP
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    def on_mouse_press(self, x, y, button, modifiers):

        # Image from PNG-EGG
        sword = arcade.Sprite("sword.png", SWORD_SCALE)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y + 30
        sword.center_x = start_x
        sword.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        sword.angle = math.degrees(angle + 340)

        sword.change_x = math.cos(angle) * SWORD_SPEED
        sword.change_y = math.sin(angle) * SWORD_SPEED

        self.sword_list.append(sword)

    def on_update(self, delta_time):

        if self.lives > 0 or self.score < 55:

            self.time_taken += delta_time

            self.physics_engine.update()

            self.player_list.update()
            self.player_list.update_animation()

            self.sword_list.update()

            # Room Logic and Setup
            if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
                self.current_room = 1
                self.room_coins = 1
                self.enemy_room = 1
                self.golden_room = 1
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = 0

            elif self.player_sprite.center_x < 0 and self.current_room == 1:
                self.current_room = 0
                self.room_coins = 0
                self.enemy_room = 0
                self.golden_room = 0
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = SCREEN_WIDTH
                self.player_sprite.center_y = SPRITE_SIZE * 4.5

            elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
                self.current_room = 2
                self.room_coins = 2
                self.enemy_room = 2
                self.golden_room = 2
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = 0
                self.player_sprite.center_y = SPRITE_SIZE * 5

            elif self.player_sprite.center_x < 0 and self.current_room == 2:
                self.current_room = 1
                self.room_coins = 1
                self.enemy_room = 1
                self.golden_room = 1
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = SCREEN_WIDTH

            # Player starting movement state
            self.player_sprite.change_x = 0
            # Player precise movement logic
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = MOVEMENT_SPEED

            # Coin logic to increase score and eliminating sprite from list
            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.coins[self.room_coins].coin_list)
            for coin in good_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_hit_sound)

            # Coin logic to increase score and eliminating sprite from list
            if len(self.enemies[self.enemy_room].enemy_list) == 0:
                good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                     self.golden[self.golden_room].golden_list)
                for golden in good_hit_list:
                    golden.remove_from_sprite_lists()
                    self.score += 5
                    arcade.play_sound(self.good_hit_sound)

            # Player lives logic to subtract a live each time sprite touches sprite
            self.dead_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                      self.enemies[self.enemy_room].enemy_list)
            for enemy in self.dead_hit_list:
                self.lives -= 1
                print(self.lives)
            #     arcade.play_sound()

            for sword in self.sword_list:

                good_hit_list = arcade.check_for_collision_with_list(sword, self.enemies[self.enemy_room].enemy_list)
                bad_hit_list = arcade.check_for_collision_with_list(sword, self.rooms[self.current_room].wall_list)

                if len(good_hit_list) > 0:
                    sword.remove_from_sprite_lists()

                for enemy in good_hit_list:
                    enemy.remove_from_sprite_lists()
                    self.score += 1

                    arcade.play_sound(self.good_hit_sound)

                if len(bad_hit_list) > 0:
                    sword.remove_from_sprite_lists()
                # for wall in bad_hit_list:
                #     arcade.play_sound(self.bad_hit_sound)

            if self.lives <= 0:
                game_over_view = GameOverView()
                game_over_view.time_taken = self.time_taken
                self.window.set_mouse_visible(True)
                self.window.show_view(game_over_view)

            if self.score == 55:
                win_view = WinView()
                win_view.time_taken = self.time_taken
                self.window.set_mouse_visible(True)
                self.window.show_view(win_view)


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75, arcade.color.WHITE,
                         font_size=50, anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE,
                         font_size=24, anchor_x="center")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         SCREEN_WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class WinView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You Won!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75, arcade.color.WHITE,
                         font_size=50, anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE,
                         font_size=24, anchor_x="center")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         SCREEN_WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.play_sound(background_soundtrack)
    arcade.run()


if __name__ == "__main__":
    main()
