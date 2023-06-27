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

# manim -pql Wrong_Lhospital.py Wrong_Lhospital -r 1080,1920

class Wrong_Lhospital(Scene):
    def construct(self):
        
        background = ImageMobject("/Users/anaemiliadeorellana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        # self.bring_to_back(background)
        title = Text('Problemathic', font_size=130, font='Chalkduster')

        title2 = Text('Let\'s study a common error in applying', font_size=60).shift(UP)
        title2_1 = Text('L\'hostpital\'s Rule', font_size=60)


        title3 = Text('Find the error in the following limit').shift(UP*4)

        expression = r"""
        \begin{align*}
        \lim_{x\to1}\frac{x^3 + x - 2}{x^2 - 3x + 2} &=  \lim_{x\to1}\frac{3x^2 + 1}{2x - 3} \\
        &= \lim_{x\to1}\frac{6x}{2} \\
        &= 3
        \end{align*}
        """

        equation = Tex(expression).scale(1.6)

        spotText = Text('Did you spot it?', font_size = 50).shift(DOWN*7)
        plotText = Text('Let\'s look at the plot', font_size = 50).shift(DOWN*8)

        axes = Axes(
            x_range=[-2, 1.2, 1],
            y_range=[-5, 1.5, 1],
            x_length=10,
            x_axis_config={
                "numbers_to_include": np.arange(-2, 1.5, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-5, 1.5, 1),
            },
            tips=True,
        ).shift(7*DOWN)
        axes_labels = axes.get_axis_labels().shift(DOWN*7)
        
        def func(x):
            return (x**3 + x - 2)/(x**2 - 3*x + 2)
    
        graph = axes.plot(func, color=GREEN_B)

        label = axes.get_graph_label(
            graph, "f(x) = \\frac{x^3 + x - 2}{x^2 - 3x + 2}", x_val=-2
        )

        plot = VGroup(axes, graph)
        labels = VGroup(axes_labels, label)

        textDot = Text('The correct answer is -4', color=RED_C).shift(11*DOWN)
        initial_point = [axes.coords_to_point(1,-4)]
        dot = Dot(point=initial_point, color=RED_C, radius=0.15)
        
        textError = Text('So where is the error?', font_size=60).shift(6*UP)
        textError2 = Text('Let\'s see the calculation again', font_size=60).shift(5*UP)

        
        seleccion=VGroup(equation[0][21:33])
        frameBox = SurroundingRectangle(seleccion, buff = 2*SMALL_BUFF).shift(DOWN)
        frameBox.set_stroke(GREEN_B,9)

        arr =  Arrow(buff=2, start=2*RIGHT+UP, end=2*LEFT+5*DOWN, color=GREEN_B)

        solution = Text('This limit is not an indeterminate form!').shift(4*DOWN)

        
        eqq = MathTex(r'\lim_{x\to1}\frac{3x^2 + 1}{2x - 3} = -4', color=GREEN_B).scale(1.6).shift(6*DOWN)
        solution2 = Text('The error was aplying L\'hospital\'s Rule twice!').shift(8*DOWN)

        self.play(Write(title))
        self.wait(0.2)
        self.play(title.animate.scale(0.2).to_edge(LEFT).shift(12*DOWN))
        self.play(Write(title2))
        self.play(Write(title2_1))
        self.wait()
        self.play(title2.animate.shift(6.5*UP),title2_1.animate.shift(6.5*UP))
        self.play(Write(title3))
        self.play(Write(equation))
        self.wait(2)
        self.play(Write(spotText))
        self.wait(0.2)
        self.play(Write(plotText))
        self.wait(0.2)
        self.play(FadeOut(spotText, plotText))
        self.play(FadeIn(plot, labels))
        self.wait()
        self.play(FadeIn(dot), FadeIn(textDot))
        self.wait()
        self.play(FadeOut(dot,textDot, plot, labels, title3, title2_1, title2))
        self.play(Write(textError), Write(textError2), equation.animate.shift(DOWN))
        self.wait()
        self.play(FadeIn(frameBox))
        self.wait()
        self.play(FadeIn(arr), FadeIn(solution))
        self.wait()
        self.play(Write(eqq))
        self.play(Write(solution2))
        self.wait()
        self.play(FadeOut(eqq, solution2, arr, frameBox, textError, textError2, equation, solution))