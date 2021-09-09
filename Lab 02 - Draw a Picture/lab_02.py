import arcade

# Opens window.
arcade.open_window(800, 800, "Lab 2 Drawing")

# Set the background and color.
arcade.set_background_color(arcade.csscolor.BLACK)

# Get ready to draw.
arcade.start_render()

# Code will go here.
# Circumference of the Yin-Yang
arcade.draw_circle_outline(400, 400, 300, arcade.csscolor.SNOW, 5)

# Yang division and coloring.
arcade.draw_parabola_filled(400, 20, 700, 380, arcade.csscolor.SNOW)
arcade.draw_parabola_filled(400, 20, 700, 380, arcade.csscolor.SNOW, 180)
arcade.draw_ellipse_filled(575, 300, 200, 300, arcade.csscolor.SNOW, 30)

# Second part of the division arc, aka negative parabola
arcade.draw_parabola_outline(100, 20, 400, 380, arcade.csscolor.SNOW, 10, 180)

# Finish drawing.
arcade.finish_render()

# Keeps the program running.
arcade.run()


