import random
import arcade

SPRITE_SCALING = 0.15
SPRITE_NATIVE_SIZE = 528
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Lab 9 Sprite and Walls"
SKE_ICON = 5

MOVEMENT_SPEED = 5

GRAVITY = 4
P_JUMP = 150

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

CHARACTER_SCALING = 5


class PlayerCharacter(arcade.Sprite):

    def __init__(self):
        # Set up parent class
        super().__init__(hit_box_algorithm='Simple')

        self.scale = SPRITE_SCALING
        self.textures = []

        texture = arcade.load_texture("soldier_idle.png")
        self.textures.append(texture)
        texture = arcade.load_texture("soldier_idle.png",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = self.textures[RIGHT_FACING]

    def update(self):

        if self.change_x < 0:
            self.texture = self.textures[LEFT_FACING]
        elif self.change_x > 0:
            self.texture = self.textures[RIGHT_FACING]


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

        super().__init__()

        self.change_x = 0

        self.enemy_list = None

    def update(self):

        self.center_x += self.change_x


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
    enemies = arcade.Sprite("metalslug_zombie.gif", SPRITE_SCALING * 2.2)
    enemies.center_x = (SCREEN_WIDTH - (SPRITE_SIZE - 25))
    enemies.bottom = SPRITE_SIZE * 4
    enemy.enemy_list.append(enemies)

    return enemy


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
                wall = arcade.Sprite("wall1.png", SPRITE_SCALING * 1.4)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # --- Place walls with a list
    coordinate_list = [[140, 285], [140, 225], [140, 165], [140, 110], [195, 225], [195, 165], [195, 110],
                       [250, 165], [250, 110], [250, 110], [305, 110]]

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
        enemies = arcade.Sprite("metalslug_zombie.gif", SPRITE_SCALING * 2.2)
        enemies.center_x = x
        enemies.bottom = SPRITE_SIZE
        enemy.enemy_list.append(enemies)

    return enemy


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
                wall = arcade.Sprite("wall1.png", SPRITE_SCALING * 1.4)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    coordinate_list = [[140, 285], [140, 225], [140, 165], [140, 110], [195, 225], [195, 165], [195, 110], [250, 165],
                       [250, 110], [250, 110], [305, 110]]

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


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # Sprite lists
        self.current_room = 0
        self.room_coins = 0
        self.enemy_room = 1

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.coins = None
        self.enemies = None
        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.score = 0

        self.good_hit_sound = arcade.sound.load_sound(":resources:sounds/coin1.wav")

    def setup(self):

        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = SPRITE_SIZE * 2
        self.player_sprite.center_y = SPRITE_SIZE * 1.5
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []
        self.coins = []
        self.enemies = []

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

        # Our starting room number
        self.current_room = 0
        self.room_coins = 0
        self.enemy_room = 0

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

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 30)

        if self.score == 30:
            arcade.draw_text("Game Over",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 80,
                             anchor_x="center")

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

    def on_update(self, delta_time):

        if self.score < 30:

            self.physics_engine.update()

            self.player_sprite.update()

            if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
                self.current_room = 1
                self.room_coins = 1
                self.enemy_room = 1
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = 0

            elif self.player_sprite.center_x < 0 and self.current_room == 1:
                self.current_room = 0
                self.room_coins = 0
                self.enemy_room = 0
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = SCREEN_WIDTH
                self.player_sprite.center_y = SPRITE_SIZE * 4.5

            elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
                self.current_room = 2
                self.room_coins = 2
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = 0
                self.player_sprite.center_y = SPRITE_SIZE * 5

            elif self.player_sprite.center_x < 0 and self.current_room == 2:
                self.current_room = 1
                self.room_coins = 1
                self.enemy_room = 1
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=GRAVITY)
                self.player_sprite.center_x = SCREEN_WIDTH

            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = MOVEMENT_SPEED

            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.coins[self.room_coins].coin_list)
            for coin in good_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_hit_sound)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
