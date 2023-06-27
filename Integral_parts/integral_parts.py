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
            r"\left(f\cdot g\right)'", font_size = 85
            )
        equation1 = MathTex(
            r"f'\cdot g + f\cdot g'", font_size = 85
            )
        eq_sign_1 =Tex('=', font_size = 60)
        equation01 = MathTex(
            r"\int_a^b \left(f\cdot g\right)'\,dx", font_size = 60
            )
        equation01_colored = MathTex(
        r"\int_a^b \left(f\cdot g\right)'\,dx", font_size = 60
        )
        equation001_colored = MathTex(
            r"(f\cdot g)(b) - (f\cdot g)(a)", font_size = 60
            )
        equation001 = MathTex(
            r"(f\cdot g)(b) - (f\cdot g)(a)", font_size = 60
            )
        equation2 = MathTex(
            r"\int_a^b \left(f'\cdot g + f\cdot g'\right)\,dx", font_size = 55
            )
        equation2_colored = MathTex(
            r"\int_a^b \left(f'\cdot g + f\cdot g'\right)\,dx", font_size = 55
            )
        equation3= MathTex(
            r"\int_a^b f'\cdot g\,dx", font_size = 55
            )
        equation3_colored= MathTex(
            r"\int_a^b f'\cdot g\,dx", font_size = 55
            )
        equation03 = MathTex(
          r"+\int_a^b f\cdot g'\,dx", font_size = 55
        )
        equation03_colored = MathTex(
          r"+\int_a^b f\cdot g'\,dx", font_size = 55
        )
        equation03_bis = MathTex(
          r"-\int_a^b f\cdot g'\,dx", font_size = 55
        )
        equation003 = MathTex(
          r"(f\cdot g)(b) - (f\cdot g)(a)-\int_a^b f\cdot g'\,dx =\int_a^b f'\cdot g\,dx", font_size = 60
        )
        eqfinal = MathTex(
            r"\int_a^b f'\cdot g\,dx =(f\cdot g)(b) - (f\cdot g)(a)-\int_a^b f\cdot g'\,dx", font_size = 60
        )
        equv = MathTex(
            r"\int u\,dv =uv-\int v\,du", font_size = 80
        )


        # Aligning in same row
        equation0.next_to(eq_sign_1, LEFT)
        equation01.next_to(eq_sign_1, LEFT)
        equation01_colored.next_to(eq_sign_1, LEFT)
        equation001.next_to(eq_sign_1, LEFT)
        equation001_colored.next_to(eq_sign_1, LEFT)
        equation1.next_to(eq_sign_1, RIGHT)
        equation2.next_to(eq_sign_1, RIGHT)
        equation2_colored.next_to(eq_sign_1, RIGHT)
        equation3_colored.next_to(eq_sign_1, RIGHT)
        equation3.next_to(eq_sign_1, RIGHT)
        equation03_bis.next_to(equation001, RIGHT)
        
        # Shift
        equation03.shift(RIGHT*4.5)
        equation03_colored.shift(RIGHT*4.5)
        equation03_bis.shift(LEFT*1.4)
        # equation01.shift(LEFT*2)
        # equation01_colored.shift(LEFT*2)
        # equation001.shift(LEFT*2)
        # equation001_colored.shift(LEFT*2)
        # equation0_colored.shift(RIGHT)
        # eq_sign_colored.shift(RIGHT)
        

        # Coloring equations
        equation01_colored[0][:].set_color(YELLOW)
        equation001_colored[0][:].set_color(YELLOW)
        equation2_colored[0][:].set_color(YELLOW)
        equation3_colored[0][:].set_color(YELLOW)
        equation03_colored[0][:].set_color(YELLOW)
        eqfinal[0][:].set_color(BLUE)
        equv[0][:].set_color(BLUE)

        eq_group = VGroup(equation0, eq_sign_1)
        eq3goup = VGroup(equation3, equation03)
        eq3goup_colored = VGroup(equation3_colored, equation03_colored)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.5)
        self.play(Write(equation1))
        self.wait(1)
        self.play(ReplacementTransform(equation1, equation2), ReplacementTransform(equation0,equation01))
        self.wait(1)
        self.play(ReplacementTransform(equation01,equation01_colored))
        self.wait(0.5)
        self.play(ReplacementTransform(equation01_colored, equation001_colored))
        self.wait(0.5)
        self.play(ReplacementTransform(equation001_colored, equation001))
        self.wait(0.5)
        self.play(ReplacementTransform(equation2, equation2_colored))
        self.wait(1)
        self.play(ReplacementTransform(equation2_colored, eq3goup_colored))
        self.wait(0.5)
        self.play(ReplacementTransform(eq3goup_colored, eq3goup))
        self.wait(1)
        self.play(equation001.animate.shift(LEFT*1.4), ReplacementTransform(equation03, equation03_bis), equation3.animate.shift(RIGHT*1.6), eq_sign_1.animate.shift(RIGHT*1.6))
        self.wait(1)
        self.play(FadeOut(equation001), FadeOut(eq_sign_1), FadeOut(equation3), ReplacementTransform(equation03_bis,eqfinal))
        self.wait(1)
        self.play(ReplacementTransform(eqfinal, equv))
        self.wait(2)
        self.play(FadeOut(equv))
        self.wait(1)
 
