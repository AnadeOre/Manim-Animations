from manim import * 
import sys
import numpy
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


class Lorenz_Attractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range= [-3.5,3.5], y_range=[-3.5,3.5], z_range=[0,6],axis_config={"include_tip": True,"include_ticks":True,"stroke_width":1})
        dot = Sphere(radius=0.05,fill_color=BLUE).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)
        
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES,gamma = 90*DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.05)            #Start move camera

        dtime = 0.01
        numsteps = 30

        self.add(axes,dot)

        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s*(y - x)
            y_dot = r*x - y - x*z
            z_dot = x*y - b*z
            return x_dot, y_dot, z_dot

        def update_trajectory(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        traj = VMobject()
        traj.start_new_path(dot.get_center())
        traj.set_stroke(BLUE, 1.5, opacity=0.8)
        traj.add_updater(update_trajectory)
        self.add(traj)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
            x = x_dot * dt/10
            y = y_dot * dt/10
            z = z_dot * dt/10
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

        dot.add_updater(update_position)
        # self.wait(420)
        
        s=10
        r=28
        b=2.667
        x =1
        y =1 
        z =1
        dt = 0.01
        for i in range(1500):
            dx = s*(y - x)
            dy = r*x - y - x*z
            dz = x*y - b*z
            x = x +dx
            y = y +dy
            z = z +dz
            self.play(dot.animate.move_to(self.coords_to_point(x,y)), run_time = 0.001, rate_function = linear)

        self.wait(3)


    

