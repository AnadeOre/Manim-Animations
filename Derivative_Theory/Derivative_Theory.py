from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk    

from manim import config as global_config
config = global_config.copy()
config.frame_height = 1920
config.frame_width = 1080

class Derivative(ThreeDScene):
    def construct(self):
        
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=130, font='Chalkduster')
        
        axes = (
            Axes (
                x_range=[0, 10, 1],
                x_length=9,
                y_range=[0, 20, 5],
                y_length=6,
                axis_config={"include_numbers":True, "include_tip":False},
            )
            .set_color(WHITE)
            # .scale(1.2)
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        # .scale(1.2)

        func = axes.plot(
            lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0, 10], color=BLUE_D
        )
        # .scale(1.2)
        
        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="dy",
                secant_line_color=GREEN,
                secant_line_length=8,
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            # .scale(0.7)
            # .scale(1.2)
            .move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            # .scale(0.7)
            # .scale(1.2)
            .move_to(
                axes.c2p(
                    (x).get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )
        scaling = VGroup(axes, axes_labels, func, secant, dot1, dot2)
        scaling.scale(1.2)

        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(FadeIn(VGroup(axes, axes_labels, func)))
        self.play(FadeIn(secant), FadeIn(dot1), FadeIn(dot2))
        self.play(dx.animate.set_value(0.001), run_time=8)
        self.wait(0.5)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait()
        self.play(x.animate.set_value(5), run_time=5)
        self.wait()
        self.play(dx.animate.set_value(3), run_time=6)
        self.wait()
        self.play(FadeOut(VGroup(secant, dot1, dot2, func, axes_labels, axes)))