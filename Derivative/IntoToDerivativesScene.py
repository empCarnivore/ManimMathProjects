#Graphics and Animation
from FormatedScene import *

class IntroToDerivativesScene(FormatedScene):
    def plot_f(self):
        zoom_tracker = ValueTracker(100)
        x_tracker = ValueTracker(.5)
        change_x_tracker = ValueTracker(.2)
        f = lambda x: x ** 2
        y_tracker = ValueTracker(.25)
        y_tracker.add_updater(lambda x: x.set_value(f(x_tracker.get_value())))

        shift_y_x = lambda y: lambda x: y(x - x_tracker.get_value())
        shift_y_y = lambda y: lambda x: y(x) - y_tracker.get_value()
        rshift_y_x = lambda y: lambda x: y(x + x_tracker.get_value())
        rshift_y_y = lambda y: lambda x: y(x) + y_tracker.get_value()
        zoom_y_0 = lambda y: lambda x: zoom_tracker.get_value() * y(x / zoom_tracker.get_value())
        zoomed_f = rshift_y_y(shift_y_x(zoom_y_0(shift_y_y(rshift_y_x(f)))))

        axes = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 1, 1],
            x_length=3,
            y_length=3,
            tips=False,
        )
        curve = axes.plot(zoomed_f, [0, 1, .1])

        increment_curve = axes.plot(zoomed_f, x_range=[x_tracker.get_value(),
                                                       x_tracker.get_value() + change_x_tracker.get_value()],
                                    color=GREEN)
        increment_curve.add_updater(
            lambda x: x.become(
                axes.plot(zoomed_f,
                          x_range=[x_tracker.get_value(), x_tracker.get_value() + change_x_tracker.get_value()],
                          color=GREEN)))

        start_point = Dot(axes.i2gp(x_tracker.get_value(), curve), color=BLUE)
        start_point.add_updater(lambda x: x.become(Dot(axes.i2gp(x_tracker.get_value(), curve), color=BLUE)))

        end_point = Dot(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), curve), color=GREEN)
        end_point.add_updater(lambda x: x.become(
            Dot(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), curve), color=GREEN)))

        h_line = axes.plot(lambda x: y_tracker.get_value())
        h_line.add_updater(lambda x: x.become(axes.plot(lambda x: y_tracker.get_value())))

        x_change_line = Line(axes.i2gp(x_tracker.get_value(), h_line),
                             axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), h_line), color=RED)
        x_change_line.add_updater(lambda x: x.become(Line(axes.i2gp(x_tracker.get_value(), h_line), axes.i2gp(
            x_tracker.get_value() + change_x_tracker.get_value(), h_line), color=RED)))

        y_change_line = Line(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), h_line),
                             axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), curve), color=YELLOW)
        y_change_line.add_updater(lambda x: x.become(
            Line(axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), h_line),
                 axes.i2gp(x_tracker.get_value() + change_x_tracker.get_value(), curve), color=YELLOW)))

        self.add(VGroup(curve, increment_curve, x_change_line, y_change_line, start_point, end_point))

    def construct(self):
        self.plot_f()

if __name__ == '__main__':
    scene = IntroToDerivativesScene()
    scene.render(True)