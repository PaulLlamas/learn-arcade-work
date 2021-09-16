import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200

def draw_computer(x, y):
    arcade.draw_triangle_filled(x - 10, y - 65, x, y - 30, x + 10, y - 65, arcade.csscolor.BLACK)
    arcade.draw_rectangle_outline(x, y, 120, 80, arcade.csscolor.SILVER, 10)
    arcade.draw_rectangle_filled(x, y, 110, 70, arcade.csscolor.WHITE_SMOKE)

def draw_table(x, y, z):
    arcade.draw_rectangle_filled(x, y, 300, 10, arcade.csscolor.PERU)
    arcade.draw_rectangle_filled(x - 135,y - 50, 20, 100, arcade.csscolor.PERU, z)
    arcade.draw_rectangle_filled(x + 135, y - 50, 20, 100, arcade.csscolor.PERU, z)

def draw_floor():
    arcade.draw_rectangle_filled(600, 400, SCREEN_WIDTH, 800, arcade.csscolor.DARK_GRAY)

def draw_boards():
    arcade.draw_rectangle_filled(325, 1000, 550, 200, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(885, 1000, 550, 200, arcade.csscolor.WHITE)

def draw_chair(x, y):
    arcade.draw_triangle_filled(x, y - 100, x - 25, y - 135, x + 25, y - 135, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x, y - 50, 110, 130, arcade.csscolor.CORNSILK)
    arcade.draw_circle_filled(x - 25, y - 135, 10, arcade.csscolor.GAINSBORO)
    arcade.draw_circle_filled(x + 25, y - 135, 10, arcade.csscolor.GAINSBORO)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3 Drawing Computer Lab")
    arcade.set_background_color(arcade.csscolor.LINEN)
    arcade.start_render()

    draw_floor()
    draw_boards()
    draw_table(250, 800, 180)
    draw_table(575, 800, 180)
    draw_table(900, 800, 180)
    draw_table(250, 500, 180)
    draw_table(575, 500, 180)
    draw_table(900, 500, 180)
    draw_table(250, 200, 180)
    draw_table(575, 200, 180)
    draw_table(900, 200, 180)
    draw_computer(250, 270)
    draw_computer(250, 570)
    draw_computer(250, 870)
    draw_computer(575, 270)
    draw_computer(575, 570)
    draw_computer(575, 870)
    draw_computer(900, 270)
    draw_computer(900, 570)
    draw_computer(900, 870)
    draw_chair(250, 200)
    draw_chair(250, 500)
    draw_chair(250, 800)
    draw_chair(575, 200)
    draw_chair(575, 500)
    draw_chair(575, 800)
    draw_chair(900, 200)
    draw_chair(900, 500)
    draw_chair(900, 800)


    # Finish drawing and run.
    arcade.finish_render()
    arcade.run()

main()