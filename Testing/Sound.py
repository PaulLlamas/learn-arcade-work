import arcade

arcade.open_window(600, 600, "Sound demo")
laser_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
arcade.play_sound(laser_sound)
arcade.run()