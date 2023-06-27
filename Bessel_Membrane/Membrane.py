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

from scipy import special
import numpy as np

# manim -pql Membrane.py Membrane -r 1080,1920

class Membrane(ThreeDScene):
    def construct(self):
        
        background = ImageMobject("/Users/anaemiliadeorellana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)
        title = Text('Problemathic', font_size=130, font='Chalkduster')

        besselTitle = Text('Bessel functions', font_size=80, font='Chalkduster').shift(6*UP)
        besselEQ = MathTex(r"J_{\alpha}(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m!\,\Gamma(m+\alpha+1)}\left( \frac{x}{2} \right)^{2m+\alpha}", font_size = 60).shift(2.5*UP)

        def u_mn(r, theta, t=0, m=2, n=0):
            a = 11.6198 #Es el coeficiente nu, que representa la tensión del material
            A=B=C=D=1 #Esto es cuánto lo estira
            return 0.4*(A*np.cos(a*t) + B*np.sin(a*t))*special.jv(m,a*r)*(C*np.cos(m*theta) + D*np.sin(m*theta))

        def f(dt=0):
            obj = Surface(lambda r, theta: np.array([r*np.cos(theta),r*np.sin(theta),u_mn(r,theta,dt)]), u_range=(-1e-5,1), v_range=(0,TAU), checkerboard_colors=['#FFFA8C', '#B6AF21'])
            obj.scale(4).rotate(angle=dt*PI/2, axis=OUT).rotate(angle=-PI/3, axis=RIGHT).shift(3*DOWN)
            return obj

        current = f()

        def update_membrane(current, alpha):
            dt = interpolate(0,1, alpha)
            new = f(dt)
            current.become(new)

        self.play(Write(title))
        self.play(FadeOut(title))
        self.play(FadeIn(current),FadeIn(besselTitle), Write(besselEQ))
        # self.wait()
        self.play(UpdateFromAlphaFunc(current, update_membrane), rate_func=linear, run_time=6)
        # self.wait()