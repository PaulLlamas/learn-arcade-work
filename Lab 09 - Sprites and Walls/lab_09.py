"""
Sprite move between different rooms.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""

import arcade

SPRITE_SCALING = 0.15
SPRITE_NATIVE_SIZE = 528
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Lab 9 Sprite and Walls"
SKE_ICON = 5

MOVEMENT_SPEED = 5

GRAVITY = 2
P_JUMP = 120

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

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("soldier_idle.png")
        self.textures.append(texture)
        texture = arcade.load_texture("soldier_idle.png",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = self.textures[RIGHT_FACING]

    def update(self):

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[LEFT_FACING]
        elif self.change_x > 0:
            self.texture = self.textures[RIGHT_FACING]


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


class Coin(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.coin_list = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
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
    brick.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(brick)

    # --- Place boxes inside a loop
    for x in range(180, 830, 120):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 350
        room.wall_list.append(brick)
    for x in range(180, 830, 120):
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.4)
        brick.center_x = x
        brick.center_y = 600
        room.wall_list.append(brick)

    # --- Place walls with a list
    coordinate_list = [[1000, 285], [1000, 225], [1000, 165], [1000, 110], [945, 225], [945, 165], [945, 110],
                       [890, 165], [890, 110], [835, 110]]

    # Loop through coordinates
    for coordinate in coordinate_list:
        brick = arcade.Sprite("dunbrick.png", SPRITE_SCALING * 1.55)
        brick.center_x = coordinate[0]
        brick.center_y = coordinate[1]
        room.wall_list.append(brick)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture("dun1.png")

    return room


def setup_coins_1():
    coin = Coin()
    coin.coin_list = arcade.SpriteList()
    for x in range(180, 830, 120):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = 650
        coin.coin_list.append(coins)
    for x in range(300, 800, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
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
        coins.center_y = 370
        coin.coin_list.append(coins)
    for x in range(300, 800, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


def setup_room_3():
    """
    Create and return room 3d.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
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

    # --- Place walls with a list
    coordinate_list = [[140, 285], [140, 225], [140, 165], [140, 110], [195, 225], [195, 165], [195, 110], [250, 165],
                       [250, 110], [250, 110], [305, 110]]

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

    room.background = arcade.load_texture("dun3.jpg")

    return room

def setup_coins_3():
    coin = Coin()
    coin.coin_list = arcade.SpriteList()
    for x in range(300, 950, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = 650
        coin.coin_list.append(coins)
    for x in range(300, 800, 150):
        coins = arcade.Sprite("skeleton.png", SPRITE_SCALING * 1.4)
        coins.center_x = x
        coins.center_y = SPRITE_SIZE + 30
        coin.coin_list.append(coins)

    return coin


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.current_room = 0
        self.current_coins = 0
        self.coin_room = []

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.coin_list = None
        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.score = 0

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = SPRITE_SIZE * 2
        self.player_sprite.center_y = SPRITE_SIZE * 1.5
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        coins = setup_coins_1()
        self.coin_room.append(coins)
        coins = setup_coins_2()
        self.coin_room.append(coins)
        coins = setup_coins_3()
        self.coin_room.append(coins)

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list,
                                                             gravity_constant=GRAVITY)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.
        self.coin_room[self.current_coins].coin_list.draw()
        self.player_list.draw()
        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 30)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.player_sprite.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list,
                                                                 gravity_constant=GRAVITY)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list,
                                                                 gravity_constant=GRAVITY)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list,
                                                                 gravity_constant=GRAVITY)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x < 0 and self.current_room == 2:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list,
                                                                 gravity_constant=GRAVITY)
            self.player_sprite.center_x = SCREEN_WIDTH

        if self.current_room == 0:
            self.current_coins = 0

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = P_JUMP
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in good_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.good_hit_sound)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
