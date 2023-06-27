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
class Fibonacci(Scene):
    def construct(self):
        background = ImageMobject("/Users/anaemiliadeorellana/Documents/Personales/Problemathic/Manim/Reel.png")
        self.add(background)
        self.bring_to_back(background)

        title = Text('Problemathic', font_size=130, font='Chalkduster')


        sequence_1 = MathTex(r"1", font_size = 100)
        sequence_1_copy = MathTex(r"1", font_size = 100)
        comma_1 = MathTex(",", font_size = 100)
        sequence_2 = MathTex(r"1", font_size = 100)
        sequence_2_copy = MathTex(r"1", font_size = 100)
        comma_2 = MathTex(",", font_size = 100)
        sequence_3 = MathTex("2", font_size = 100)
        sequence_3_copy = MathTex(r"2", font_size = 100)
        comma_3 = MathTex(",", font_size = 100)
        sequence_4 = MathTex("3", font_size = 100)
        sequence_4_copy = MathTex("3", font_size = 100)
        comma_4 = MathTex(",", font_size = 100)
        sequence_5 = MathTex("5", font_size = 100)
        sequence_5_copy = MathTex("5", font_size = 100)
        comma_5 = MathTex(",", font_size = 100)
        sequence_6 = MathTex("8", font_size = 100)
        sequence_6_copy = MathTex("8", font_size = 100)
        comma_6 = MathTex(",", font_size = 100)
        sequence_7 = MathTex("13", font_size = 100)
        sequence_7_copy = MathTex("13", font_size = 100)
        comma_7 = MathTex(",", font_size = 100)
        sequence_8 = MathTex("21", font_size = 100)
        sequence_8_copy = MathTex("21", font_size = 100)
        comma_8 = MathTex(",", font_size = 100)
        sequence_9 = MathTex("34", font_size = 100)
        sequence_9_copy = MathTex("34", font_size = 100)
        comma_9 = MathTex(",", font_size = 100)
        dots_sequence = MathTex(r"\cdots", font_size = 100)

        F1 = MathTex(r"F_1 = 1", font_size = 100)
        F2 = MathTex(r"F_2 = 1", font_size = 100)
        F3 = MathTex(r"F_3 = F_2 + F_1 = 2", font_size = 100)
        F4 = MathTex(r"F_4 = F_3 + F_2 = 3", font_size = 100)
        F5 = MathTex(r"F_5 = F_4 + F_3 = 5", font_size = 100)
        F6 = MathTex(r"F_6 = F_5 + F_4 = 8", font_size = 100)
        F7 = MathTex(r"F_7 = F_6 + F_5 = 13", font_size = 100)
        F8 = MathTex(r"F_8 = F_7 + F_6 = 21", font_size = 100)
        F9 = MathTex(r"F_9 = F_8 + F_7 = 34", font_size = 100) 

        F3[0][3:5].set_color("#04d9ff")
        F3[0][6:8].set_color("#04d9ff")
        F4[0][3:5].set_color("#04d9ff")
        F4[0][6:8].set_color("#04d9ff")
        F5[0][3:5].set_color("#04d9ff")
        F5[0][6:8].set_color("#04d9ff")
        F6[0][3:5].set_color("#04d9ff")
        F6[0][6:8].set_color("#04d9ff")
        F7[0][3:5].set_color("#04d9ff")
        F7[0][6:8].set_color("#04d9ff")
        F8[0][3:5].set_color("#04d9ff")
        F8[0][6:8].set_color("#04d9ff")
        F9[0][3:5].set_color("#04d9ff")
        F9[0][6:8].set_color("#04d9ff")        
        
        seqGroup = VGroup(sequence_1_copy, sequence_2_copy, sequence_3_copy,
                          sequence_4_copy, sequence_5_copy, sequence_6_copy,
                          sequence_7_copy, sequence_8_copy, sequence_9_copy)
        commasGroup = VGroup(comma_1, comma_2, comma_3, comma_4, comma_5, comma_6, comma_7,
                             comma_8, comma_9, dots_sequence)
        eqsGroup = VGroup(F1, F2, F3, F4, F5, F6, F7, F8, F9)
        
        seqGroup.shift(LEFT*1.8, UP*2)
        commasGroup.shift(DOWN*0.5, UP*2)
        eqsGroup.shift(DOWN*2)

        def shift_to_corner_custom(equation, toTransform, prevNum, n1, n2, comma): 
            equation.shift(DOWN)
            if prevNum == 1:
                toTransform.shift(3.7*LEFT)
            else:
                toTransform.next_to(prevNum, 2*RIGHT)
            if n1!= 0:
                self.play(AnimationGroup(
                    Write(equation)),
                    n1[0].animate.set_color("#04d9ff"),
                    n2[0].animate.set_color("#04d9ff")
                )
                self.play(
                Transform(equation, toTransform),
                n1[0].animate.set_color(WHITE),
                n2[0].animate.set_color(WHITE)
                )
            else:
                self.play(Write(equation))
                self.play(
                    Transform(equation, toTransform))
            comma.next_to(toTransform, 0.5*RIGHT)
            comma.shift(0.2*DOWN)
            self.play(Write(comma), run_time=0.1)

        
        FibSequence = [1, 2, 3, 5, 8, 13, 21, 34, 55]
        nextDir = [DOWN, LEFT, UP, RIGHT]
        squares = VGroup(Square(0.5*0.3))
        squares.shift(DOWN)

        for j, i in enumerate(FibSequence):
            d = nextDir[j % 4]
            squares.add(Square(i/2 * 0.3).next_to(squares, d, buff=0))

        squares.center()
        direction = [1, 1, -1, -1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle = -PI / 2 *d,
                color = "#04d9ff",
                stroke_width = 6,
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)

        spiral.shift(DOWN*3)
        squares.shift(DOWN*3)
        # Animation
        self.play(Write(title))
        self.play(FadeOut(title))
               
        shift_to_corner_custom(F1, sequence_1_copy, 1,0,0, comma_1)
        shift_to_corner_custom(F2, sequence_2_copy, sequence_1_copy, 0, 0, comma_2)
        shift_to_corner_custom(F3, sequence_3_copy, sequence_2_copy, sequence_2_copy, sequence_1_copy, comma_3)
        shift_to_corner_custom(F4, sequence_4_copy, sequence_3_copy, sequence_3_copy, sequence_2_copy, comma_4)
        shift_to_corner_custom(F5, sequence_5_copy, sequence_4_copy, sequence_4_copy, sequence_3_copy, comma_5)
        shift_to_corner_custom(F6, sequence_6_copy, sequence_5_copy, sequence_5_copy, sequence_4_copy, comma_6)
        shift_to_corner_custom(F7, sequence_7_copy, sequence_6_copy, sequence_6_copy, sequence_5_copy, comma_7)
        shift_to_corner_custom(F8, sequence_8_copy, sequence_7_copy, sequence_7_copy, sequence_6_copy, comma_8)
        shift_to_corner_custom(F9, sequence_9_copy, sequence_8_copy, sequence_8_copy, sequence_7_copy, comma_9)
        dots_sequence.next_to(sequence_9_copy, 2*RIGHT)
        self.play(Write(dots_sequence))
        self.play(
            F1.animate.shift(3.2*UP),
            comma_1.animate.shift(3.2*UP),
            F2.animate.shift(3.2*UP),
            comma_2.animate.shift(3.2*UP),
            F3.animate.shift(3.2*UP),
            comma_3.animate.shift(3.2*UP),
            F4.animate.shift(3.2*UP),
            comma_4.animate.shift(3.2*UP),
            F5.animate.shift(3.2*UP),
            comma_5.animate.shift(3.2*UP),
            F6.animate.shift(3.2*UP),
            comma_6.animate.shift(3.2*UP),
            F7.animate.shift(3.2*UP),
            comma_7.animate.shift(3.2*UP),
            F8.animate.shift(3.2*UP),
            comma_8.animate.shift(3.2*UP),
            F9.animate.shift(3.2*UP),
            comma_9.animate.shift(3.2*UP),
            dots_sequence.animate.shift(3.2*UP),
            FadeOut(sequence_1_copy, run_time=0.1),
            FadeOut(sequence_2_copy, run_time=0.1),
            FadeOut(sequence_3_copy, run_time=0.1),
            FadeOut(sequence_4_copy, run_time=0.1),
            FadeOut(sequence_5_copy, run_time=0.1),
            FadeOut(sequence_6_copy, run_time=0.1),
            FadeOut(sequence_7_copy, run_time=0.1),
            FadeOut(sequence_8_copy, run_time=0.1),
            FadeOut(sequence_9_copy, run_time=0.1)
            )
        self.wait(0.2)
        self.play(
            LaggedStart(FadeIn(squares, lag_ratio=1), Create(spiral, lag_ratio=1), run_time=5))
        self.wait(3)
