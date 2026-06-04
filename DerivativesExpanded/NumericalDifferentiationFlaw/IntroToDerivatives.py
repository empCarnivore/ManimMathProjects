# Graphics and Animation

from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class IntroToDerivatives(FormatedScene):
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
        a=0
        START_ZOOM = 1
        zoom_tracker = ValueTracker(START_ZOOM)
        change_x_tracker = ValueTracker(.2)
        x_tracker = ValueTracker(0)
        y_tracker = ValueTracker(1)
        # endregion

        # region graph functions
        g = lambda x: (x**4-1)/(x-1)
        f = lambda x, x0, y0, z: (g(a+x)-g(a))/x
        d_f_a = 3*a**2+2*a+1
        shift_y_x = lambda y: lambda x, x0, y0, z: y(x - x0, x0, y0, z)
        shift_y_y = lambda y: lambda x, x0, y0, z: y(x, x0, y0, z) - y0
        rshift_y_x = lambda y: lambda x, x0, y0, z: y(x + x0, x0, y0, z)
        rshift_y_y = lambda y: lambda x, x0, y0, z: y(x, x0, y0, z) + y0
        zoom_y_0 = lambda y: lambda x, x0, y0, z: z * y(x / z, x0, y0, z)
        zoomed_f = rshift_y_y(shift_y_x(zoom_y_0(shift_y_y(rshift_y_x(f)))))

        # endregion

        # region axes
        axes = Axes(
            x_range=[-1, 1/3, 1],
            y_range=[-1, 2, 1],
            x_length=3,
            y_length=3,
            tips=False,
            axis_config={"include_ticks":False}
        )
        axes_label=axes.get_axis_labels(x_label="h",y_label="")

        axes2 = deepcopy(axes)
        # endregion

        # region point

        point_coordinates = axes.coords_to_point(0, d_f_a)
        point = Dot(point_coordinates)
        point.set_color(CYAN1)

        # endregion

        # region curve
        curve = axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),use_smoothing=False,color=CYAN1)

        curve.add_updater(lambda o: o.become(
            axes.plot(lambda x: zoomed_f(x, x_tracker.get_value(), y_tracker.get_value(), zoom_tracker.get_value()),use_smoothing=False,color=CYAN1)
        ))

        # endregion

        graph = VGroup(axes_label,axes,curve,point)

        # endregion

        # region titles
        title1 = Title("Derivatives 101")
        # endregion

        # region math tex construction

        # region math2 construct
        math2 = VGroup()
        math2 += MathTex(r"{{ \lim_{ h \to 0} }} { {{y}}(x+{{h}})-{{y}}(x) \over {{h}} } = {{y}}'(x) {{\iff}} {{y}}(x+{{\Delta x}}) \approx {{y}}(x) + {{\Delta x}} y'(x)")
        math2 += MathTex(r"{{f(h)}} = { y(a + {{h}} )-y(a) \over {{h}} }")
        math2[0].set_color(CYAN1)
        # endregion

        # region math3 construct
        math1 = VGroup()
        math1 += MathTex(r"{{ \text{Given } }} {{\Delta x}} {{ \text{ is small, then: } }}")
        math1 += MathTex(r"y(x)= {x^4-1 \over x-1} ")
        # endregion

        math3 = VGroup()
        math3 += MathTex(r"a = "+str(a))

        math4 = VGroup()
        math4 += MathTex(r"y'(a) = "+str(d_f_a))


        mathvg = VGroup(*math1, *math2,*math3,*math4)


        # region global math colors
        deep_set_color_by_tex(mathvg, r"\Delta x", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"h", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"f(h)", CYAN1)
        deep_set_color_by_tex(mathvg, r"\text{ is small, then: }", WHITE)
        deep_set_color_by_tex(mathvg, r"\iff", WHITE)
        deep_set_color_by_tex(mathvg, r"=", WHITE)
        deep_set_color_by_tex(mathvg, r"\approx", WHITE)
        deep_set_color_by_tex(mathvg, r"\lim_{ h \to 0}", WHITE)
        # endregion


        # region tex locations
        math1.next_to(title1, DOWN)
        math2.next_to(math1, DOWN)
        graph.next_to(math2,DOWN*1.5)
        math3.next_to(graph,LEFT,buff=1)
        math4.next_to(math3,DOWN)
        # endregion

        self.play(Write(title1))

        self.play(Write(math1[0]))
        self.play(Write(math2[0]))

        self.wait(10)

        self.play(FadeOut(math1[0]),FadeOut(math2[0]))

        self.play(Write(math1[1]))
        self.play(Write(math2[1]))


        self.play(Create(graph))
        self.play(Write(math3[0]))
        self.play(Write(math4[0]))

        self.wait(5)

        self.play(zoom_tracker.animate.set_value(10), run_time=2)


if __name__ == '__main__':
    scene = IntroToDerivatives()
    scene.render(True)
