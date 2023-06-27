from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

class Limit_one_over_e(Scene):
    def construct(self):
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Limit_one_over_e/Background.jpg")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=100, font='CHAWP')
        equation1 = MathTex(
            r'\lim\limits_{n\to\infty}\left(1-\frac{1}{n}\right)^n'
            )
        eq_sign_1 =Tex('=')
        equation2 = MathTex(
            r'\lim\limits_{n\to\infty}\left(\frac{n-1}{n}\right)^{n}'
            )
        equation3 = MathTex(
            r'\lim\limits_{n\to\infty}\left(\frac{1}{\frac{n}{n-1}}\right)^{n}'
            )
        equation4 = MathTex(
            r'\lim\limits_{n\to\infty}\frac{1}{\left(\frac{n}{n-1}\right)^{n}}'
            )
        equation5 = MathTex(
            r'\lim\limits_{n\to\infty}\frac{1}{\left(\frac{n-1+1}{n-1}\right)^{n}}'
            )
        equation6 = MathTex(
            r'\lim\limits_{n\to\infty}\frac{1}{\left(1+\frac{1}{n-1}\right)^{n}}'
            )
        equation7 = MathTex(
            r'\lim\limits_{n\to\infty}\frac{1}{\left(1+\frac{1}{n-1}\right)^{n-1+1}}'
            )
        equation8 = MathTex(
            r'\lim\limits_{n\to\infty}\frac{1}{\left(1+\frac{1}{n-1}\right)^{n-1}\left(1+\frac{1}{n-1}\right)^{1}}'
            )
        equation9 = MathTex(
            r'\frac{1}{e\cdot 1}'
            )
        equation10 = MathTex(
            r'\frac{1}{e}'
            )
        equation10_colored = MathTex(
            r'\frac{1}{e}'
            )
        equation1_colored = MathTex(
            r'\lim\limits_{n\to\infty}\left(1-\frac{1}{n}\right)^n'
            )
        eq_sign_colored = MathTex("=")

        # Aligning in same row
        equation1.next_to(eq_sign_1, LEFT)
        equation1_colored.next_to(eq_sign_colored, LEFT)
        equation2.next_to(eq_sign_1, RIGHT)
        equation3.next_to(eq_sign_1)
        equation4.next_to(eq_sign_1)
        equation5.next_to(eq_sign_1)
        equation5.next_to(eq_sign_1)
        equation6.next_to(eq_sign_1)
        equation7.next_to(eq_sign_1)
        equation8.next_to(eq_sign_1)
        equation9.next_to(eq_sign_1)
        equation10.next_to(eq_sign_1)
        equation10_colored.next_to(eq_sign_1)
        
        # Shift to Left
        equation2.shift(LEFT*2)
        equation3.shift(LEFT*2)
        equation4.shift(LEFT*2)
        equation5.shift(LEFT*2)
        equation6.shift(LEFT*2)
        equation7.shift(LEFT*2)
        equation8.shift(LEFT*2)
        equation9.shift(LEFT*2)
        equation10.shift(LEFT*2)
        equation1_colored.shift(RIGHT)
        equation10_colored.shift(RIGHT)
        eq_sign_colored.shift(RIGHT)
        

        # Coloring equations
        equation5[0][10:14].set_color(RED)
        equation7[0][18:22].set_color(RED)
        equation8[0][17:20].set_color(RED)
        equation8[0][-1].set_color(RED)
        equation10_colored.set_color(BLUE)
        equation1_colored.set_color(BLUE)
        eq_sign_colored.set_color(BLUE)

        eq_group = VGroup(equation1, eq_sign_1)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.5)
        self.play(eq_group.animate.shift(LEFT*2))
        self.play(Write(equation2))
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
        self.wait(0.3)
        self.play(ReplacementTransform(equation10, equation10_colored),ReplacementTransform(eq_sign_1, eq_sign_colored), ReplacementTransform(equation1, equation1_colored))
        self.wait(2)
