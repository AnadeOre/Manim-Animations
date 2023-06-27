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

class KochCurve(Scene):
    def construct(self):
        background = ImageMobject("/Users/anaemiliadeorellana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        title = Text('Problemathic', font_size=130, font='Chalkduster')
        perimeter = Text('Perimeter')
        area = Text('Area')
        perTex = MathTex(r'= + \infty')
        areaTex = MathTex(r'< + \infty')
        LastVid = Text('Watch our videos to learn why', font_size=50 , font='CHAWP')

        Perimeter = VGroup(perimeter, perTex)
        Area = VGroup(area, areaTex)

        perTex.shift(UP+RIGHT)
        perimeter.next_to(perTex, LEFT)
        areaTex.shift(DOWN+RIGHT)
        area.next_to(areaTex, LEFT)

        def KochCurve(
            n, length=5, stroke_width=8, color=("#f01d1d", "#ff6969", "#f01d1d") 
        ):

            l = length / (3 ** n)

            LineGroup = Line().set_length(l)

            def NextLevel(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

            for _ in range(n):
                LineGroup = NextLevel(LineGroup)

            KC = (
                VMobject(stroke_width=stroke_width)
                .set_points(LineGroup.get_all_points())
                .set_color(color)
            )
            return KC

        level = Variable(0, Tex("Iteration", font_size=60), var_type=Integer).set_color("#ff6969")
        txt = (
            VGroup(Tex("Koch Curve", font_size=90), level)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL).shift(3*UP)
        )
        kc = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5).rotate(angle=PI, about_point=ORIGIN).shift(DOWN*3.4)
        kc1 = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5).rotate(angle=-60*PI/180, about_point=ORIGIN).shift(RIGHT*2.52+ UP)
        kc2 = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5).rotate(angle=60*PI/180, about_point=ORIGIN).shift(LEFT*2.52+ UP)

        self.play(Write(title))
        self.play(FadeOut(title))
        self.play(FadeIn(txt), FadeIn(kc), FadeIn(kc1), FadeIn(kc2))
        self.wait()

        for i in range(1, 6):
            self.play(
                level.tracker.animate.set_value(i),
                kc.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=PI, about_point=ORIGIN).shift(DOWN*3.4),
                kc1.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=-60*PI/180, about_point=ORIGIN).shift(RIGHT*2.52 + UP),
                kc2.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=60*PI/180, about_point=ORIGIN).shift(LEFT*2.52 + UP),
            )
            self.wait()

        for i in range(4, -1, -1):
            self.play(
                level.tracker.animate.set_value(i),
                kc.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=PI, about_point=ORIGIN).shift(DOWN*3.4),
                kc1.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=-60*PI/180, about_point=ORIGIN).shift(RIGHT*2.52 + UP),
                kc2.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ).rotate(angle=60*PI/180, about_point=ORIGIN).shift(LEFT*2.52 + UP),
            )
            self.wait()
        self.play(FadeOut(txt), FadeOut(kc), FadeOut(kc1), FadeOut(kc2))
        self.play(Write(Perimeter), Write(Area))
        self.wait(2)
        self.play(Unwrite(Perimeter), Unwrite(Area))
        self.play(Write(LastVid))
        self.wait()
        self.play(FadeOut(LastVid))



