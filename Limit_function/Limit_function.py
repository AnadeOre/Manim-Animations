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
class Limit_function(Scene):
    def construct(self):
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=130, font='CHAWP')
        equation1 = MathTex(
            r'\lim\limits_{x\to\infty}\frac{x-1}{2x^2+3}', font_size = 115
            )
        equation1_colored = MathTex(
            r'\lim\limits_{x\to\infty}\frac{x-1}{2x^2+3}', font_size = 120
            )
        eq_sign_1 =Tex('=', font_size = 115)
        eq_sign_below = Tex('=', font_size = 110)
        equation2 = MathTex(
            r'\lim\limits_{x\to\infty}\frac{x-1}{2x^2+3}\cdot\frac{x^2}{x^2}', font_size = 110
            )
        equation3 = MathTex(
            r'\lim\limits_{x\to\infty}\frac{\frac{x-1}{x^2}}{\frac{2x^2+3}{x^2}}', font_size = 110
            )
        equation4 = MathTex(
            r'\lim\limits_{x\to\infty}\frac{\frac{x}{x^2}-\frac{1}{x^2}}{\frac{2x^2}{x^2}+\frac{3}{x^2}}', font_size = 110
            )
        equation5= MathTex(
            r'\lim\limits_{x\to\infty}\frac{\frac{1}{x}-\frac{1}{x^2}}{2+\frac{3}{x^2}}', font_size = 110
            )
        equation6 = MathTex(
            r'\frac{0-0}{2+0}', font_size = 110
            )
        equation7 = MathTex(
            r'\frac{0}{2}', font_size = 110
            )
        equation8 = MathTex(
            r'0', font_size = 110
            )
        equation8_colored = MathTex(
            r'0', font_size = 120
            )
        eq_sign_colored = MathTex("=", font_size = 120)

        # Aligning in same row
        eq_sign_1.shift(RIGHT*0.5)
        equation1.next_to(eq_sign_1, LEFT)
        eq_sign_colored.shift(RIGHT*2)
        equation1_colored.next_to(eq_sign_colored, LEFT)
        eq_sign_below.shift(DOWN*2, LEFT*3)
        equation2.next_to(eq_sign_below, RIGHT)
        equation3.next_to(eq_sign_below)
        equation4.next_to(eq_sign_below)
        equation5.next_to(eq_sign_below)
        equation6.next_to(eq_sign_below)
        equation7.next_to(eq_sign_below)
        equation8.next_to(eq_sign_below)
        equation8_colored.next_to(eq_sign_colored)
        
        # Shift to Left+)
        # equation3.shift(BELOW*2)
        # equation4.shift(BELOW*2)
        # equation5.shift(BELOW*2)
        # equation6.shift(BELOW*2)
        # equation7.shift(RIGHT*0.5)
        # equation8.shift(RIGHT*0.5)
        equation1_colored.shift(RIGHT)
        equation8_colored.shift(RIGHT)
        eq_sign_colored.shift(RIGHT)
        

        # Coloring equations
        equation2[0][15:21].set_color(YELLOW)
        equation3[0][9:12].set_color(YELLOW)
        equation3[0][18:21].set_color(YELLOW)
        equation4[0][6:10].set_color(YELLOW)
        equation4[0][17:22].set_color(YELLOW)
        equation5[0][0:9].set_color(YELLOW)
        equation5[0][10:14].set_color(YELLOW)
        equation5[0][18:22].set_color(YELLOW)
        equation6[0][0].set_color(YELLOW)
        equation6[0][2].set_color(YELLOW)
        equation6[0][6].set_color(YELLOW)
        equation8_colored.set_color(BLUE)
        equation1_colored.set_color(BLUE)
        eq_sign_colored.set_color(BLUE)

        eq_group = VGroup(equation1, eq_sign_1)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.5)
        self.play(eq_group.animate.shift(UP*2.5))
        self.play(Write(eq_sign_below),Write(equation2))
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
        self.wait(0.3)
        self.play(FadeOut(eq_sign_below),ReplacementTransform(equation8, equation8_colored),ReplacementTransform(eq_sign_1, eq_sign_colored), ReplacementTransform(equation1, equation1_colored))
        self.wait(2)
