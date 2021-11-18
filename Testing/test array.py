import arcade
import random

WIDTH = 60
HIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # Create a grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[2][9] = 1

        print(self.grid)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HIGHT / 2 + row * (HIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = arcade.color.BABY_BLUE_EYES

                arcade.draw_rectangle_filled(x, y, WIDTH, HIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        print(f"You clicked on {row} coordinate and {column} coordinate")

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()