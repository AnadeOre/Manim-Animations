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
class Integral_e_x_2(Scene):
    def construct(self):
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=130, font='Chalkduster')
        
        
        equation0 = MathTex(
            r'\int_{-\infty}^{\infty}e^{-x^2}dx', font_size = 90
            )
        equation01 = MathTex(
            r'\int_{-\infty}^{\infty}e^{-x^2}dx', font_size = 100
            )
        equation0_colored = MathTex(
            r'\int_{-\infty}^{\infty}e^{-x^2}dx', font_size = 100
            )
        equation1 = MathTex(
            r'\left(\int_{-\infty}^{\infty}e^{-x^2}\, dx\right)^2', font_size = 85
            )
        eq_sign_1 =Tex('=', font_size = 100)
        eq_sign_2 =Tex('=', font_size = 100)
        eq_sign_3 =Tex('=', font_size = 100)
        equation2 = MathTex(
            r'\int_{-\infty}^{\infty}e^{-x^2}\, dx\,\cdot\,\int_{-\infty}^{\infty}e^{-x^2}\, dx', font_size = 90
            )
        equation3 = MathTex(
            r'\int_{-\infty}^{\infty}e^{-x^2}\, dx\,\cdot\int_{-\infty}^{\infty}e^{-y^2}\, dy', font_size = 90
            )
        equation4 = MathTex(
            r'\int_{-\infty}^{\infty}\left(\int_{-\infty}^{\infty}e^{-x^2}\,dx\right)e^{-y^2}\, dy', font_size = 90
            )
        equation5= MathTex(
            r'\int_{-\infty}^{\infty}\left(\int_{-\infty}^{\infty}e^{-(x^2+y^2)}\,dx\right)\, dy', font_size = 90
            )
        equation6 = MathTex(
            r'\int_{-\infty}^{\infty}\,\int_{-\infty}^{\infty}e^{-(x^2+y^2)}\,dx\, dy', font_size = 100
            )
        equation7 = MathTex(
            r'\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\,dx\, dy', font_size = 100
            )
        equation8 = MathTex(
            r'\int_{0}^{2\pi}\int_{0}^{\infty}re^{-r^2}\,dr\, d\theta', font_size = 100
            )
        equation9 = MathTex(
            r'\int_{0}^{2\pi}d\theta\cdot\int_{0}^{\infty}re^{-r^2}\,dr', font_size = 100
            )
        equation10 = MathTex(
            r'2\pi\cdot\int_{0}^{\infty}re^{-r^2}\,dr', font_size = 100
            )
        equation11 = MathTex(
            r'2\pi\cdot\int_{-\infty}^{0}\frac{1}{2}e^{s}\,ds', font_size = 100
            )
        equation12 = MathTex(
            r'\pi\cdot\int_{-\infty}^{0}\,e^{s}\,ds', font_size = 100
            )
        equation13 = MathTex(
            r'\pi(e^{0}-e^{-\infty})', font_size = 100
            )
        equation14 = MathTex(
            r'\pi(1-0)', font_size = 100
            )
        equation15 = MathTex(
            r'\pi', font_size = 100
            )
        equation16 = MathTex(
            r'\sqrt{\pi}', font_size = 100
            )
        equation16_colored = MathTex(
            r'\sqrt{\pi}', font_size = 100
            )

        eq_sign_colored = MathTex(
            r'=', font_size = 100
        )


        # Aligning in same row
        equation0.next_to(eq_sign_1, LEFT)
        equation01.next_to(eq_sign_1, LEFT)
        equation0_colored.next_to(eq_sign_1, LEFT)
        equation1.next_to(eq_sign_1, LEFT)
        equation2.next_to(eq_sign_2, RIGHT)
        equation3.next_to(eq_sign_2)
        equation4.next_to(eq_sign_2)
        equation5.next_to(eq_sign_2)
        equation6.next_to(eq_sign_2)
        equation7.next_to(eq_sign_2)
        equation8.next_to(eq_sign_2)
        equation9.next_to(eq_sign_2)
        equation10.next_to(eq_sign_2)
        equation11.next_to(eq_sign_2)
        equation12.next_to(eq_sign_2)
        equation13.next_to(eq_sign_2)
        equation14.next_to(eq_sign_2)
        equation15.next_to(eq_sign_2)
        equation16.next_to(eq_sign_2)
        equation16_colored.next_to(eq_sign_2)

        
        # Shift to Left
        # eq_sign_1.shift(UP*2)
        # equation01.shift(UP*2)
        eq_sign_2.shift(LEFT*6)
        equation2.shift(LEFT*6)
        equation3.shift(LEFT*6)
        equation4.shift(LEFT*6)
        equation5.shift(LEFT*6)
        equation6.shift(LEFT*6)
        equation7.shift(LEFT*6)
        equation8.shift(LEFT*6)
        equation9.shift(LEFT*6)
        equation10.shift(LEFT*6)
        equation11.shift(LEFT*6)
        equation12.shift(LEFT*6)
        equation13.shift(LEFT*6)
        equation14.shift(LEFT*6)
        equation15.shift(LEFT*6)
        equation16.shift(RIGHT)
        equation16_colored.shift(RIGHT)
        equation0_colored.shift(RIGHT)
        eq_sign_colored.shift(RIGHT)
        

        # Coloring equations
        equation2[0][17:18].set_color(YELLOW)
        equation2[0][20:21].set_color(YELLOW)
        equation3[0][17:18].set_color(YELLOW)
        equation3[0][20:21].set_color(YELLOW)
        equation4[0][10:13].set_color(YELLOW)
        equation4[0][17:20].set_color(YELLOW)
        equation5[0][10:18].set_color(YELLOW)
        equation8[0][0:4].set_color(RED)
        equation8[0][14:16].set_color(RED)
        equation9[0][0:6].set_color(RED)
        equation10[0][0:2].set_color(RED)
        equation10[0][3:13].set_color(YELLOW)
        equation11[0][0:1].set_color(RED)
        equation11[0][3:9].set_color(YELLOW)
        equation11[0][9:10].set_color(RED)
        equation11[0][10:14].set_color(YELLOW)
        equation12[0][2:10].set_color(YELLOW)
        equation13[0][1:9].set_color(YELLOW)
        equation14[0][1:6].set_color(YELLOW)
        equation16_colored.set_color(BLUE)
        equation0_colored.set_color(BLUE)
        eq_sign_colored.set_color(BLUE)

        eq_group = VGroup(equation0, eq_sign_1)
        eq_group0 = VGroup(equation01, eq_sign_1)
        eq_group1 = VGroup(equation1, eq_sign_1)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.5)
        self.play(ReplacementTransform(equation0, equation1))
        self.wait(0.5)
        self.play(eq_group1.animate.shift(UP*4))
        self.play(Write(eq_sign_2), Write(equation2))
        self.wait(1)
        self.play(ReplacementTransform(equation2, equation3))
        self.wait(1)
        self.play(ReplacementTransform(equation3, equation4))
        self.wait(1)
        self.play(ReplacementTransform(equation4, equation5))
        self.wait(1)
        self.play(ReplacementTransform(equation5, equation6))
        self.wait(1)
        self.play(ReplacementTransform(equation6, equation7))
        self.wait(1)
        self.play(ReplacementTransform(equation7, equation8))
        self.wait(1)
        self.play(ReplacementTransform(equation8, equation9))
        self.wait(1)
        self.play(ReplacementTransform(equation9, equation10))
        self.wait(1)
        self.play(ReplacementTransform(equation10, equation11))
        self.wait(1)
        self.play(ReplacementTransform(equation11, equation12))
        self.wait(1)
        self.play(ReplacementTransform(equation12, equation13))
        self.wait(1)
        self.play(ReplacementTransform(equation13, equation14))
        self.wait(1)
        self.play(ReplacementTransform(equation14, equation15))
        self.wait(1)
        # self.play(ReplacementTransform(eq_sign_2, eq_sign_3), ReplacementTransform(equation15, equation16), ReplacementTransform(equation1, equation01))
        self.wait(0.5)
        # self.play(ReplacementTransform(equation16, equation16_colored),ReplacementTransform(eq_sign_1, eq_sign_colored), ReplacementTransform(equation01, equation0_colored))
        self.play(ReplacementTransform(equation15, equation16_colored),FadeOut(eq_sign_2), ReplacementTransform(eq_sign_1, eq_sign_colored), ReplacementTransform(equation1, equation0_colored))
        self.wait(2)
