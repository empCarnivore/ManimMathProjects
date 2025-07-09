#Graphics and Animation
from FormatedScene import *

class IntroToDerivativesScene(FormatedScene):
    def construct(self):
        START_ZOOM=10
        zoom_tracker = ValueTracker(START_ZOOM)
        change_x_tracker = ValueTracker(.2)
        f = lambda x,x0,y0,z: x ** 2
        x_tracker = ValueTracker(.5)
        y_tracker = ValueTracker(.25)

        shift_y_x = lambda y: lambda x,x0,y0,z: y(x - x0,x0,y0,z)
        shift_y_y = lambda y: lambda x,x0,y0,z: y(x,x0,y0,z) - y0
        rshift_y_x = lambda y: lambda x,x0,y0,z: y(x + x0,x0,y0,z)
        rshift_y_y = lambda y: lambda x,x0,y0,z: y(x,x0,y0,z) + y0
        zoom_y_0 = lambda y: lambda x,x0,y0,z: z * y(x / z,x0,y0,z)
        zoomed_f = rshift_y_y(shift_y_x(zoom_y_0(shift_y_y(rshift_y_x(f)))))

        axes = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 1, 1],
            x_length=3,
            y_length=3,
            tips=False,
        )
        curve = axes.plot(lambda x: zoomed_f(x,x_tracker.get_value(),y_tracker.get_value(),zoom_tracker.get_value()), [0, 1, .1])

        curve.add_updater(lambda o: o.become(
            axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),
                      [0, 1, .1])
        ))

        increment_curve = axes.plot(lambda x: zoomed_f(x,x_tracker.get_value(),y_tracker.get_value(),zoom_tracker.get_value()), x_range=[x_tracker.get_value(),
                                                       x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM],
                                    color=GREEN)
        increment_curve.add_updater(
            lambda o: o.become(
                axes.plot(lambda x: zoomed_f(x,x_tracker.get_value(),y_tracker.get_value(),zoom_tracker.get_value()),
                          x_range=[x_tracker.get_value(), x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM],
                          color=GREEN)))

        start_point = Dot(axes.i2gp(x_tracker.get_value(), curve), color=BLUE)
        start_point.add_updater(lambda o: o.become(Dot(axes.i2gp(x_tracker.get_value(), curve),radius=DEFAULT_DOT_RADIUS*zoom_tracker.get_value()/START_ZOOM, color=BLUE)))

        end_point = Dot(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, curve), color=GREEN)
        end_point.add_updater(lambda o: o.become(
            Dot(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, curve),radius=DEFAULT_DOT_RADIUS*zoom_tracker.get_value()/START_ZOOM, color=GREEN)))

        h_line = axes.plot(lambda x: y_tracker.get_value())
        h_line.add_updater(lambda o: o.become(axes.plot(lambda x: y_tracker.get_value())))

        x_change_line = Line(axes.i2gp(x_tracker.get_value(), h_line),
                             axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, h_line), color=RED)
        x_change_line.add_updater(lambda o: o.become(Line(axes.i2gp(x_tracker.get_value(), h_line), axes.i2gp(
            x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, h_line), color=RED)))

        y_change_line = Line(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, h_line),
                             axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, curve), color=YELLOW)
        y_change_line.add_updater(lambda o: o.become(
            Line(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, h_line),
                 axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value()*zoom_tracker.get_value()/START_ZOOM, curve), color=YELLOW)))

        graph=VGroup(curve, increment_curve, x_change_line, y_change_line, start_point, end_point)

        title1=Title("Straight Lines 101")

        self.add(title1)

        math1_2=MathTex(r"{{y(x+\Delta x)}}= {{y(x)}} + {{{\Delta y}}\over{{\Delta x}}} {{\Delta x}}")

        math1_1 = MathTex(r"{{y(x+\Delta x)}}= {{y(x)}} + {{m}} {{\Delta x}}")

        math1_1.set_color_by_tex(r"\Delta x",RED)
        math1_1.set_color_by_tex(r"\Delta y", YELLOW)
        math1_1.set_color_by_tex(r"h", RED)
        math1_1.set_color_by_tex(r"y(x)", BLUE)
        math1_1.set_color_by_tex(r"y(x+\Delta x)",GREEN)

        math1_2.set_color_by_tex(r"\Delta x", RED)
        math1_2.set_color_by_tex(r"\Delta y", YELLOW)
        math1_2.set_color_by_tex(r"h", RED)
        math1_2.set_color_by_tex(r"y(x)", BLUE)
        math1_2.set_color_by_tex(r"y(x+\Delta x)", GREEN)

        math2=MathTex(r"{{{\Delta y}}\over{{\Delta x}}} = {{m}}")

        math2.set_color_by_tex(r"\Delta x", RED)
        math2.set_color_by_tex(r"\Delta y", YELLOW)
        math2.set_color_by_tex(r"h", RED)
        math2.set_color_by_tex(r"y(x)", BLUE)
        math2.set_color_by_tex(r"y(x+h)", GREEN)

        math1_1.next_to(title1,DOWN)
        math1_2.next_to(title1, DOWN)
        math2.next_to(curve,LEFT)

        self.add(math1_1)

        self.add(math2)

        self.add(graph)

        self.wait(2)

        #self.play(zoom_tracker.animate.set_value(1),run_time=2)

        #self.wait(2)

if __name__ == '__main__':
    scene = IntroToDerivativesScene()
    scene.render(True)