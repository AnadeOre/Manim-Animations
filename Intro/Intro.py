from doctest import run_docstring_examples
from math import factorial
from manim import * 
import sys

from numpy import angle
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

class IntroVid(Scene):
    def construct(self):
        background = ImageMobject("/home/ana/Documents/Personales/Problemathic/Manim/Limit_one_over_e/Background.jpg")
        self.add(background)
        self.bring_to_back(background)

        Name = Text('Problemathic', font_size=100, font='CHAWP')
        Outro = Text('Come Study with us', font_size=50, font="CHAWP")
        Euler = MathTex(
            r'e^{i\pi}+1 = 0'
            )
        Calculus_Fundamental = MathTex(
            r"\int_{a}^{b}f'(x)\,dx = f(b) - f(a)"
            )
        Pythagoras = MathTex(
            r'a^{2}+b^{2} = c'
        )
        Fibonacci = MathTex(
            r'F_{n} = F_{n-1} + F_{n-2}'
        )
        Euler_Spheres = MathTex(
            r'V-E+F = 2'
        )
        Minimal_Surface = MathTex(
            r'\mathcal{A} = \int_{\Omega}(1+|\nabla u|^{2})^{\frac{1}{2}}\, dx_1\cdots dx_n'
        )
        Cauchy = MathTex(
            r'(u,u)(v,v)\geq |(u,v)|^{2}'
        )
        Triangular = MathTex(
            r'|a+b|\leq |a|+|b|'
        )
        Bayes = MathTex(
            r'P(A|B) = \frac{P(B|A)P(A)}{P(B)}'
        )
        Helder = MathTex(
            r'\norm{fg}_1 \leq \norm{f}_p \norm{g}_q'
        )

        Calculus_Fundamental.shift(2.5*UP).rotate(angle=0.1*PI, about_point=ORIGIN)
        Pythagoras.shift(2*DOWN + RIGHT)
        Fibonacci.shift(3*UP+3*RIGHT).rotate(angle=-0.05*PI, about_point=ORIGIN)
        Euler_Spheres.shift(3*LEFT + 2.5*DOWN).rotate(angle=0.05*PI, about_point=ORIGIN)
        Minimal_Surface.shift(3*LEFT + 3*UP).rotate(angle=0.05*PI, about_point=ORIGIN)
        Cauchy.shift(2.5*DOWN)
        Bayes.shift(3*RIGHT + 3*UP).rotate(angle=-0.05*PI, about_point=ORIGIN)
        Triangular.shift(4.5*LEFT + 2.5*DOWN).rotate(angle=0.05*PI, about_point=ORIGIN)

        self.play(Write(Name))
        self.play(Write(Calculus_Fundamental), run_time=0.9)
        self.play(Write(Pythagoras))
        self.play(Unwrite(Calculus_Fundamental, run_time=0.9), Write(Fibonacci))
        self.play(Unwrite(Pythagoras), Write(Euler_Spheres))
        self.play(Unwrite(Fibonacci), Write(Minimal_Surface))
        self.play(Unwrite(Euler_Spheres, run_speed=0.9), Write(Cauchy))
        self.play(Unwrite(Minimal_Surface, run_speed=0.9), Write(Bayes))
        self.play(Unwrite(Cauchy), Write(Triangular))
        self.play(Unwrite(Bayes))
        self.play(Unwrite(Triangular))
        self.play(Unwrite(Name))
        self.play(Write(Outro, run_speed=1.2))
        self.play(Unwrite(Outro))

