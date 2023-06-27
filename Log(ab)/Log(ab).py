from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

class Logab(Scene):
    def construct(self):
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Limit_one_over_e/Background.jpg")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=100, font='CHAWP')
        text2 = Text('Follow us for more!', font_size=80, font='CHAWP')

        Youtube= ImageMobject("YouTubeLogo.png")
        Instagram= ImageMobject("InstagramLogo.png")
        Youtube.scale(0.05)
        Instagram.scale(0.07)


        
        equation0 = MathTex(
            r'\log(ab)', font_size=80
            )
        equation1 = MathTex(
            r'\int_1^{ab}\frac{1}{x}\, dx', font_size=80
            )
        eq_sign_1 =Tex('=', font_size=80)
        equation2 = MathTex(
            r'\int_1^{a}\frac{1}{x}\, dx + \int_a^{ab}\frac{1}{x}\, dx', font_size=80
            )
        equation3 = MathTex(
            r'\int_1^a\frac{1}{x}\, dx + \int_1^b\frac{1}{at}\,d(at)', font_size=80
            )
        equation4 = MathTex(
            r'\int_1^a\frac{1}{x}\, dx + \int_1^b \frac{1}{t}\, dt', font_size=80
            )
        equation5= MathTex(
            r'\log(a) + log(b)', font_size=80
            )


        # Aligning in same row
        equation0.next_to(eq_sign_1, LEFT)
        equation1.next_to(eq_sign_1)
        equation2.next_to(eq_sign_1)
        equation3.next_to(eq_sign_1)
        equation4.next_to(eq_sign_1)
        equation5.next_to(eq_sign_1)

        
        # Shift to Left
        equation1.shift(LEFT*2)
        equation2.shift(LEFT*2)
        equation3.shift(LEFT*2)
        equation4.shift(LEFT*2)
        equation5.shift(LEFT*2)

        Youtube.shift(LEFT + DOWN)
        Instagram.shift(RIGHT + DOWN)
        text2.shift(UP)

        # Coloring equations
        equation0[0][4:5].set_color(RED_B)
        equation0[0][5:6].set_color(YELLOW)
        equation1[0][1:2].set_color(RED_B)
        equation1[0][2:3].set_color(YELLOW)
        equation2[0][1:2].set_color(RED_B)
        equation2[0][10:11].set_color(RED_B)
        equation2[0][11:12].set_color(YELLOW)
        equation2[0][12:13].set_color(RED_B)
        equation3[0][1:2].set_color(RED_B)
        equation3[0][10:11].set_color(YELLOW)
        equation3[0][14:15].set_color(RED_B )
        equation3[0][18:19].set_color(RED_B)
        equation4[0][1:2].set_color(RED_B)
        equation4[0][10:11].set_color(YELLOW)
        equation5[0][4:5].set_color(RED_B)
        equation5[0][11:12].set_color(YELLOW)

        eq_group = VGroup(equation0, eq_sign_1)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.7)
        self.play(eq_group.animate.shift(LEFT*2))
        self.wait(0.8)
        self.play(Write(equation1))
        self.wait(1.5)
        self.play(ReplacementTransform(equation1, equation2))
        self.wait(1.5)
        self.play(ReplacementTransform(equation2, equation3))
        self.wait(1.5)
        self.play(ReplacementTransform(equation3, equation4))
        self.wait(1.5)
        self.play(ReplacementTransform(equation4, equation5))
        self.wait(1.5)
        self.play(FadeOut(equation5, eq_group))
        self.play(Write(text2))
        self.play(FadeIn(Youtube, Instagram))
        self.wait(2)
