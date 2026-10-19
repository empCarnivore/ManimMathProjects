from scipy.differentiate import derivative

from FormatedScene import *

class OverComeErrorSimple(FormatedScene):
    def construct(self):
        title = Title("A Simple Fix for Massive Improvement")

        rewrite_derivative = VGroup()
        rewrite_derivative += MathTex(r"\lim_{h \to 0} { f(x + h)-f( {{x}} ) \over {{h}} } = f'(x)")
        rewrite_derivative += MathTex(r"\lim_{h \to 0} { f(x + h)-f( {{x}}{{ - h}} ) \over {{2}}{{h}} } = f'(x)")

        first_series = VGroup()
        first_series += MathTex(r"f(x + h) = \sum_{n = 0}^\infty {h^n \over n!} f^{(n)}(x)")

        second_series = VGroup()
        second_series += MathTex(r"f(x)")
        second_series += MathTex(r"f(x - h) = \sum_{n = 0}^\infty -{(-h)^n \over n!} f^{(n)}(x)")

        third_series = VGroup()
        third_series += MathTex(r"f(x+h)-f(x) = \sum_{n = 1}^\infty {h^n \over n!} f^{(n)}(x)")

        series_error = VGroup()
        series_error += MathTex(r"{f(x+h)-f( {{x}} ) \over h} = f'(x) + O(h)")
        series_error += MathTex(r"{f(x+h)-f( {{x}} {{-h}} ) \over h} = f'(x) + O(h^2)")

        error_explanation = VGroup()
        error_explanation += MathTex(r"O(h^2) < O(h)")


        self.play(Write(title))

        self.wait()

        self.play(Write(rewrite_derivative[0]))

        self.wait()

        self.play(TransformByIndexMap(rewrite_derivative[0],rewrite_derivative[1],((),(2,4))))

        self.wait()

if __name__ == '__main__':
    scene = OverComeErrorSimple()
    scene.render(True)