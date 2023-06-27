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

# manim -pql Diff_integral.py Diff_integral -r 1080,1920


class Diff_integral(Scene):
    def construct(self):
        # Define the integral expression
        expression = MathTex(r"\int \frac{1}{\sqrt{1-x^2}} \,dx")

        # Position and scale the expression
        expression.scale(1.5)
        expression.to_edge(UP)

        # Show the expression
        self.play(Write(expression))
        self.wait(1)

        # Integrate by substitution
        step1 = MathTex(r"Let \ x = \sin(u)")
        step1.next_to(expression, DOWN, buff=1)

        step2 = MathTex(r"dx = \cos(u) \,du")
        step2.next_to(step1, DOWN)

        step3 = MathTex(r"\int \frac{1}{\sqrt{1-x^2}} \,dx = \int \frac{1}{\sqrt{1-\sin^2(u)}} \cdot \cos(u) \,du")
        step3.next_to(step2, DOWN, buff=0.8)

        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(2)

        # Simplify the integrand
        step4 = MathTex(r"=\int \frac{1}{\cos(u)} \,du")
        step4.next_to(step3, DOWN, buff=1)

        step5 = MathTex(r"=\int \sec(u) \,du")
        step5.next_to(step4, DOWN)

        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(2)

        # Apply the integral formula
        step6 = MathTex(r"=\ln|\sec(u) + \tan(u)| + C")
        step6.next_to(step5, DOWN).shift(RIGHT)

        self.play(Write(step6))
        self.wait(2)

        # Fade out the steps
        self.play(*[FadeOut(step) for step in [step1, step2, step3, step4, step5, step6]])
        self.wait(1)