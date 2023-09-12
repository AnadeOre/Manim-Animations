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


class Euler(Scene):
    def construct(self):

        background = ImageMobject("../Reel.png")
        self.add(background)
        self.bring_to_back(background)

        title = Text('Problemathic', font_size=100, font='Chalkduster')
        self.play(Write(title))
        self.play(FadeOut(title))

        title1 = Text('Euler\'s Identity', font_size=60)

        axes = ComplexPlane(
            x_range=[-2, 2],
            y_range=[-2, 2],
            # height=6.0,  # Adjust the height as needed
            # width=6.0,   # Adjust the width as needed
            axis_config={"color": BLACK},
        )
        axes.scale(3)
        self.add(axes)

        circle = Circle(radius=3, color=WHITE)
        circle.move_to(axes.get_center())

        # Create a point at (1, 0) and a point on the circle
        center = Dot(ORIGIN, color=RED)
        point_on_circle = Dot(circle.point_from_proportion(0.5), color=BLUE)

        arc = Arc(
            start_angle=0,
            angle=0,
            radius=3,
            arc_center=ORIGIN,
            color=YELLOW,
        )

        arc2 = Arc(
            start_angle=0,
            angle=PI,
            radius=3,
            arc_center=ORIGIN,
            color=YELLOW,
        )

        # Create a line connecting the center and the point on the circle
        line = Line(center.get_center(),
                    point_on_circle.get_center(), color=GREEN)

        group = VGroup(circle, center, point_on_circle, arc, line)

        # Add everything to the scene
        self.add(axes, group)

        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
        )

        # Animate the point moving around the circle and increasing the angle

        def update_elements(mob):
            angle = np.angle(complex(*point_on_circle.get_center()[:2]))

            decimal.add_updater(lambda d: d.set_value(angle))

            mob[3].become(Arc(
                start_angle=0,
                angle=angle,
                radius=3,
                arc_center=ORIGIN,
                color=YELLOW,
            ))
            mob[4].put_start_and_end_on(
                center.get_center(), point_on_circle.get_center())
        self.add(decimal)
        self.play(
            MoveAlongPath(point_on_circle, arc2,
                          rate_func=rate_functions.ease_out_expo,),
            UpdateFromFunc(group, update_elements),
            run_time=6,
        )

        self.wait(1)
