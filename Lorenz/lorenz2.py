from manim import *
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk
class Lorenz(ThreeDScene):
    def construct(self):

        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Limit_one_over_e/Background.jpg")
        self.add(background)
        self.bring_to_back(background)

        title = Text('Problemathic', font_size=100, font='CHAWP')
        self.play(Write(title))
        self.play(FadeOut(title))

        axes = Axes (
                x_range=[-50,50,100],
                y_range=[-50,50,100],
                x_axis_config = {"include_numbers":False, "include_tip":False},
                y_axis_config = {"include_numbers":False, "include_tip":False}
                # axis_config={"include_numbers":False, "include_tip":False},
            ).set_color(WHITE).add_coordinates()
       
        self.play(FadeIn(axes))

        #system variables
        ro = 28
        sigma = 10
        beta  = 8/3
        x =1
        y =1 
        z =1
        dt = 0.01
        x1 = 1.2
        y1 = 1.6
        z1 = 1.5
        dt1 = 0.01
        
        dot = Dot([x,y,0]).set_color(YELLOW)
        dot.move_to(axes.coords_to_point(x,y))
        dot1 = Dot([x,y,0]).set_color(RED)
        dot1.move_to(axes.coords_to_point(x,y))


        for i in range(1000):
            dx = sigma * (y-x) * dt
            dy = (x*(ro-z) -y)*dt
            dz =(x*y - beta * z) * dt
            x = x +dx
            y = y +dy
            z = z +dz

            dx1 = sigma * (y1-x1) * dt1
            dy1 = (x1*(ro-z1) -y1)*dt1
            dz1 =(x1*y1 - beta * z1) * dt1
            x1 = x1 +dx1
            y1 = y1 +dy1
            z1 = z1 +dz1

            self.play(dot.animate.move_to(axes.coords_to_point(x,y)), run_time = 0.0005, rate_function = linear)
            self.add(TracedPath(dot.get_center, stroke_color=YELLOW))

            self.play(dot1.animate.move_to(axes.coords_to_point(x1,y1)), run_time = 0.0005, rate_function = linear)
            self.add(TracedPath(dot1.get_center, stroke_color=RED))
        self.wait(3)