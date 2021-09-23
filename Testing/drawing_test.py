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

# Yin-Yang division and coloring.
arcade.draw_parabola_filled(400, 20, 700, 380, arcade.csscolor.SNOW)
arcade.draw_parabola_outline(100, 20, 400, 380, arcade.csscolor.SNOW, 10, 180)

# Yang coloring.
arcade.draw_parabola_filled(400, 20, 700, 380, arcade.csscolor.SNOW, 180)
arcade.draw_ellipse_filled(575, 300, 200, 300, arcade.csscolor.SNOW, 30)
arcade.draw_ellipse_filled(510, 230, 200, 300, arcade.csscolor.SNOW, 55)
arcade.draw_ellipse_filled(360, 160, 100, 250, arcade.csscolor.SNOW, 105)
arcade.draw_polygon_filled(((400, 400),
                            (400, 390),
                            (395, 370),
                            (395, 350),
                            (390, 340),
                            (365, 280),
                            (340, 250),
                            (320, 235),
                            (290, 220),
                            (380, 200),
                            (500, 350),
                            (415, 400)),
                           arcade.csscolor.SNOW)
arcade.draw_polygon_filled(((255, 208),
                            (180, 232),
                            (160, 250),
                            (145, 265),
                            (133, 285),
                            (125, 290),
                            (133, 265),
                            (145, 243),
                            (170, 210),
                            (210, 170),
                            (240, 150),
                            (270, 130),
                            (340, 110),
                            (370, 105)),
                           arcade.csscolor.SNOW)

# The Yang in the Yin.
arcade.draw_circle_filled(250, 360, 50, arcade.csscolor.SNOW)

# The Yin in the Yang.
arcade.draw_circle_filled(545, 440, 50, arcade.csscolor.BLACK)

# Yin-Yang diagonal exterior rectangles.
arcade.draw_rectangle_outline(130, 130, 50, 200, arcade.csscolor.SNOW, 10, 45)
arcade.draw_rectangle_outline(670, 670, 50, 200, arcade.csscolor.SNOW, 10, 45)
arcade.draw_rectangle_outline(670, 130, 50, 200, arcade.csscolor.SNOW, 10, 135)
arcade.draw_rectangle_outline(130, 670, 50, 200, arcade.csscolor.SNOW, 10, 135)

# Yin-Yang cardinal exterior rectangles.
arcade.draw_rectangle_outline(65, 400, 50, 425, arcade.csscolor.SNOW, 10)
arcade.draw_rectangle_outline(735, 400, 50, 425, arcade.csscolor.SNOW, 10)
arcade.draw_rectangle_outline(400, 735, 50, 425, arcade.csscolor.SNOW, 10, 90)
arcade.draw_rectangle_outline(400, 65, 50, 425, arcade.csscolor.SNOW, 10, 90)

# Finish drawing.
arcade.finish_render()

# Keeps the program running.
arcade.run()
