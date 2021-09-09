"""
Test
"""
import arcade

# It opens a window.
arcade.open_window(600, 600, "Drawing Example")

# Sets a background color.
arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

# Get ready to draw.
arcade.start_render()

# Code will go here.
arcade.draw_lrtb_rectangle_filled(0, 600, 350, 0, arcade.csscolor.GREENYELLOW)

arcade.draw_lrtb_rectangle_filled(90, 110, 350, 280, arcade.csscolor.BROWN)

arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(200, 220, 350, 280, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(210, 350, 30, arcade.csscolor.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(300, 320, 350, 280, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(300, 300, 50, 50, arcade.csscolor.DARK_GREEN)


# Finish drawing.
arcade.finish_render()

arcade.run()

