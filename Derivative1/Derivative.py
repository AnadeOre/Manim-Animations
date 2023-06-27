from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk    

# manim -pql Derivative.py Derivative
from manim import config as global_config
config = global_config.copy()
config.frame_height = 1920
config.frame_width = 1080
class Derivative(Scene):
    def construct(self):
        background = ImageMobject("/Users/anaemiliadeorellana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        text = Text('Problemathic', font_size=130, font='Chalkduster')
        
        
        equation0 = MathTex(
            r'\frac{d}{dx}\left(x^{x^x}\right)'
            )
        equation0_colored = MathTex(
            r'\frac{d}{dx}\left(x^{x^x}\right)'
            )
        equation01 = MathTex(
            r'\frac{d}{dx}\left(e^{x^{x}\log(x)}\right)'
            )
        equation1 = MathTex(
            r'e^{x^{x}\log(x)}\left(\frac{d}{dx}(x^x\log(x))\right)'
            )
        eq_sign_1 =Tex('=')
        equation2 = MathTex(
            r'x^{x^x}\frac{d}{dx}(x^x\log(x))'
            )
        equation3 = MathTex(
            r'x^{x^x}\left(\log(x)\left(\frac{d}{dx}(x^x) \right) + x^x\left(\frac{d}{dx}(\log(x)) \right)\right)'
            )
        equation4 = MathTex(
            r'x^{x^x}\left(\log(x)\left(\frac{d}{dx}\left(e^{x\log(x)} \right) \right) + x^x\left(\frac{d}{dx}(\log(x)) \right)\right)'
            )
        equation5= MathTex(
            r'x^{x^x}\left(\log(x)x^x\left(\log(x)\left(\frac{d}{dx}\left(x\right) \right)+x\left(\frac{d}{dx}(\log(x)) \right)  \right)+ x^x\left(\frac{d}{dx}(\log(x)) \right)\right)'
            )
        equation6 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x)+x\left(\frac{d}{dx}(\log(x)) \right)  \right)+ x^x\left(\frac{d}{dx}(\log(x)) \right)\right)'
            )
        equation7 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x)+x\left(\frac{d}{dx}(\log(x)) \right)  \right)+ \frac{\frac{d}{dx}(x)}{x}x^x\right)'
            )
        equation8 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x)+x\left(\frac{d}{dx}(\log(x)) \right) \right)+ x^{-1+x}\left(\frac{d}{dx}(x) \right)\right)'
            )
        equation9 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x) + \frac{\frac{d}{dx}(x)}{x}x \right)+ x^{-1+x}\right)'
            )
        equation10 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x) + \frac{d}{dx}(x) \right)+ x^{-1+x}\right)'
            )
        equation11 = MathTex(
            r'x^{x^x}\left(x^x\log(x)\left(\log(x) +1 \right)+ x^{-1+x}\right)'
            )
        equation12 = MathTex(
            r'x^{-1+x+x^x}\left(1+x\log(x) + x\log^2(x)\right)'
            )
        equation12_colored = MathTex(
            r'x^{-1+x+x^x}\left(1+x\log(x) + x\log^2(x)\right)'
            )

        eq_sign_colored = MathTex(
            r'='
        )


        # Aligning in same row
        equation0.next_to(eq_sign_1, LEFT)
        equation01.next_to(eq_sign_1, RIGHT)
        equation1.next_to(eq_sign_1, RIGHT)
        equation2.next_to(eq_sign_1, RIGHT)
        equation3.next_to(eq_sign_1)
        equation4.next_to(eq_sign_1)
        equation5.next_to(eq_sign_1)
        equation6.next_to(eq_sign_1)
        equation7.next_to(eq_sign_1)
        equation8.next_to(eq_sign_1)
        equation9.next_to(eq_sign_1)
        equation10.next_to(eq_sign_1)
        equation11.next_to(eq_sign_1)
        equation12.next_to(eq_sign_1)
        equation12_colored.next_to(eq_sign_1)
        equation0_colored.next_to(eq_sign_colored, LEFT)
        
        # Shift to Left
        equation0.shift(LEFT*2)
        eq_sign_1.shift(LEFT*2)
        equation01.shift(LEFT*4)
        equation1.shift(LEFT*4)
        equation2.shift(LEFT*4)
        equation3.shift(LEFT*4)
        equation4.shift(LEFT*5)
        equation5.shift(LEFT*7)
        equation6.shift(LEFT*6)
        equation7.shift(LEFT*5)
        equation8.shift(LEFT*5.5)
        equation9.shift(LEFT*4)
        equation10.shift(LEFT*4)
        equation11.shift(LEFT*4)
        equation12.shift(LEFT*4)
        equation12_colored.shift(LEFT*2.5)
        eq_sign_colored.shift(LEFT*2)
        equation0_colored.shift(LEFT*2)

        # Scale
        equation4.scale(0.8)
        equation5.scale(0.6)
        equation6.scale(0.7)
        equation7.scale(0.8)
        equation8.scale(0.75)
        equation12_colored.scale(0.8)

        # Colors
        equation0_colored.set_color(BLUE)
        equation12_colored.set_color(BLUE)
        eq_sign_colored.set_color(BLUE)

        eq_group = VGroup(equation0, eq_sign_1)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(eq_group))
        self.wait(0.5)
        self.play(eq_group.animate.shift(LEFT*2))
        self.play(Write(equation01))
        self.wait(1)
        self.play(ReplacementTransform(equation01, equation1))
        self.wait(1)
        self.play(ReplacementTransform(equation1, equation2))
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
        self.wait(0.3)
        self.play(ReplacementTransform(equation12, equation12_colored),ReplacementTransform(eq_sign_1, eq_sign_colored), ReplacementTransform(equation0, equation0_colored))
        self.wait(2)
