# Graphics and Animation

from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class IntroToDerivativesScene(FormatedScene):
    def construct(self):
        # region construction

        # region colors
        Y0_COLOR = DARK_BLUE
        Y1_COLOR = GREEN
        DY_COLOR = YELLOW
        DX_COLOR = RED
        SLOPED_COLOR = CYAN1
        # endregion

        # region graph construction

        # region graph variables
        START_ZOOM = 10
        zoom_tracker = ValueTracker(START_ZOOM)
        change_x_tracker = ValueTracker(.2)
        x_tracker = ValueTracker(.5)
        y_tracker = ValueTracker(.25)
        # endregion

        # region graph functions
        f = lambda x, x0, y0, z: x ** 2
        shift_y_x = lambda y: lambda x, x0, y0, z: y(x - x0, x0, y0, z)
        shift_y_y = lambda y: lambda x, x0, y0, z: y(x, x0, y0, z) - y0
        rshift_y_x = lambda y: lambda x, x0, y0, z: y(x + x0, x0, y0, z)
        rshift_y_y = lambda y: lambda x, x0, y0, z: y(x, x0, y0, z) + y0
        zoom_y_0 = lambda y: lambda x, x0, y0, z: z * y(x / z, x0, y0, z)
        zoomed_f = rshift_y_y(shift_y_x(zoom_y_0(shift_y_y(rshift_y_x(f)))))

        # endregion

        # region axes
        axes = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 1, 1],
            x_length=3,
            y_length=3,
            tips=False,
        )

        # endregion

        # region curve
        curve = axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),
                          [0, 1, .1])

        curve.add_updater(lambda o: o.become(
            axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),
                      [0, 1, .1])
        ))

        # endregion

        # region increment curve
        increment_curve = axes.plot(
            lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),
            x_range=[x_tracker.get_value(),
                     x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM],
            color=SLOPED_COLOR)
        increment_curve.add_updater(
            lambda o: o.become(
                axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),
                          x_range=[x_tracker.get_value(),
                                   x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM],
                          color=SLOPED_COLOR)))

        # endregion

        # region points

        # region starting point
        start_point = Dot(axes.i2gp(x_tracker.get_value(), curve), color=Y0_COLOR)
        start_point.add_updater(lambda o: o.become(Dot(axes.i2gp(x_tracker.get_value(), curve),
                                                       radius=DEFAULT_DOT_RADIUS * zoom_tracker.get_value() / START_ZOOM,
                                                       color=Y0_COLOR)))
        # endregion

        # region end point
        end_point = Dot(
            axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                      curve), color=Y1_COLOR)
        end_point.add_updater(lambda o: o.become(
            Dot(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                          curve), radius=DEFAULT_DOT_RADIUS * zoom_tracker.get_value() / START_ZOOM, color=Y1_COLOR)))
        # endregion

        # endregion

        # region lines

        # region change in x line

        # region horizontal line
        h_line = axes.plot(lambda x: y_tracker.get_value())
        h_line.add_updater(lambda o: o.become(axes.plot(lambda x: y_tracker.get_value())))
        # endregion

        x_change_line = Line(axes.i2gp(x_tracker.get_value(), h_line),
                             axes.i2gp(
                                 x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                                 h_line), color=DX_COLOR)
        x_change_line.add_updater(lambda o: o.become(Line(axes.i2gp(x_tracker.get_value(), h_line), axes.i2gp(
            x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM, h_line),
                                                          color=DX_COLOR)))

        # endregion

        # region change in y line
        y_change_line = Line(
            axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                      h_line),
            axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                      curve), color=DY_COLOR)
        y_change_line.add_updater(lambda o: o.become(
            Line(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                           h_line),
                 axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value() * zoom_tracker.get_value() / START_ZOOM,
                           curve), color=DY_COLOR)))
        # endregion

        # endregion

        graph = VGroup(curve, increment_curve, x_change_line, y_change_line, start_point, end_point)

        # endregion

        # region titles
        title1 = Title("Straight Lines 101")
        title2 = Title("Derivatives 101")
        # endregion

        # region math tex construction

        # region math1 construct
        math1 = VGroup()
        math1 += MathTex(r"{{y(x+\Delta x)}} = {{y(x)}} + {{m}} {{\Delta x}}")
        math1 += MathTex(r"{{y(x+\Delta x)}} = {{y(x)}} + {{\Delta y}}")
        math1 += MathTex(r"{{y(x+dx)}} = {{y(x)}} + {{dy}}")

        # endregion

        # region math2 construct
        math2 = VGroup()
        math2 += MathTex(r"{ {{\Delta y}} \over {{\Delta x}} } {{=}} {{m}}")
        math2 += MathTex(r" {{\Delta y}} {{=}} {{m}} {{\Delta x}}")
        math2 += MathTex(r" {{dy}} {{=}} {{f'(x)}} {{dx}}")
        # endregion

        # region math3 construct
        math3 = VGroup()
        math3 += MathTex(r"\text{Given } {{dx}} \text{ is infinitely small, then: }")
        # endregion

        mathvg = VGroup(*math1, *math2, *math3)

        # region global math colors
        deep_set_color_by_tex(mathvg, r"\Delta x", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"dx", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"\Delta y", DY_COLOR)
        deep_set_color_by_tex(mathvg, r"dy", DY_COLOR)
        deep_set_color_by_tex(mathvg, r"y(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"y(x+\Delta x)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"y(x+dx)", Y1_COLOR)
        # endregion

        # region tex locations
        math1.next_to(title1, DOWN)
        math2.next_to(curve, LEFT)
        math3.next_to(title2, DOWN)
        # endregion

        # endregion

        # endregion

        # region animation

        # region straight lines
        self.play(Write(title1))

        self.play(Create(graph))

        self.play(Write(math1[0]))

        self.play(Write(math2[0]))

        self.play(TransformMatchingTex(math2[0], math2[1]))

        self.play(TransformMatchingTex(math1[0], math1[1]))
        # endregion

        # region into derivative
        self.play(Unwrite(title1))
        self.play(Write(title2))

        self.play(zoom_tracker.animate.set_value(1), run_time=2)

        self.play(math1[1].animate.next_to(math3, DOWN),axes.animate.shift(DOWN/2))


        self.play(Write(math3[0]))

        math1[2].next_to(math3, DOWN)
        self.play(TransformMatchingTex(math1[1], math1[2]))
        self.play(TransformMatchingTex(math2[1], math2[2]))
        # endregion

        self.wait(1)
        # endregion


if __name__ == '__main__':
    scene = IntroToDerivativesScene()
    scene.render(True)
