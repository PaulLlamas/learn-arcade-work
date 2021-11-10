import arcade


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

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
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
                arcade.draw_rectangle_filled(x, y, WIDTH, HIGHT, arcade.color.BABY_BLUE_EYES)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()