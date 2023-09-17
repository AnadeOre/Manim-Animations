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

        title = Text('Problemathic', font_size=120, font='Chalkduster')
        self.play(Write(title))
        self.play(FadeOut(title))

        title1 = Text('Euler\'s Identity', font_size=60)

        axes = ComplexPlane(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )
        axes.scale(3)
        self.add(axes)

        circle = Circle(radius=3, color=WHITE)
        circle.move_to(axes.get_center())

        center = Dot(ORIGIN, color=RED)
        point_on_circle = Dot(circle.point_from_proportion(0), color=BLUE)

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

        line = Line(center.get_center(),
                    point_on_circle.get_center(), color=GREEN)

        group = VGroup(circle, center, point_on_circle, arc, line)
        self.add(axes, group)

        decimal = DecimalNumber(
            0,
            num_decimal_places=3,
        )

        result = DecimalNumber(
            0,
            num_decimal_places=3,
        )

        def update_elements(mob):
            angle = np.angle(complex(*point_on_circle.get_center()[:2]))

            decimal.add_updater(lambda d: d.set_value(angle))
            result.add_updater(lambda d: d.set_value(np.exp(1j*angle)+1))
            mob[3].become(Arc(
                start_angle=0,
                angle=angle,
                radius=3,
                arc_center=ORIGIN,
                color=YELLOW,
            ))
            mob[4].put_start_and_end_on(
                center.get_center(), point_on_circle.get_center())
        result.shift(UP*6.6 + RIGHT*1.8).scale(1.8)
        decimal.shift(UP*6.95 + LEFT*2.7).scale(1.1)

        eq = MathTex(r'e^{i\cdot\,\quad} + 1 =',
                     font_size=90).shift(UP*6.7 + LEFT*1.95)
        self.play(Write(eq))
        self.add(result, decimal)

        self.play(
            MoveAlongPath(point_on_circle, arc2,
                          rate_func=rate_functions.ease_in_out_quint,),
            UpdateFromFunc(group, update_elements),
            run_time=6,
        )

        self.wait(0.5)

        eq2 = MathTex(r'e^{i\pi}+1 = 0').scale(4)
        euler_text = Text('Euler\'s Identity', font_size=90,
                          font='Chalkduster').shift(3*UP)
        self.play(FadeOut(group), FadeOut(axes),
                  FadeOut(result), FadeOut(decimal), ReplacementTransform(eq, eq2))
        self.play(Write(euler_text))
